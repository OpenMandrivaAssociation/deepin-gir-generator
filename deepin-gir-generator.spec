%define   _name           go-gir
%define   import_path     github.com/linuxdeepin/go-gir

Name:           deepin-gir-generator
Version:        3.0.4
Release:        1
Summary:        Go-gir-generator imeplement static golang bindings for GObject
License:        GPL3.O
Group:          Development/Languages/Golang
Url:            https://github.com/linuxdeepin/go-gir
Source0:        https://github.com/linuxdeepin/go-gir/archive/v%{version}/%{_name}-%{version}.tar.gz

BuildRequires:  golang
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gdk-2.0)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  fdupes
Provides:       %{_name}

%description
Go-gir-generator imeplement static golang bindings for GObject.

There has many go bindings for GObject/Gtk libraries, but almost all of them 
are written by hand. It's bored and error-prone when the binding C libaray 
changed.

Go-gir-geneator's object is like python-gobject's that binding the newest 
library without need change binding codes.

Currently it only official support Gobject-2.0, Glib-2.0, Gio-2.0. Because 
generate the gdkpixbuf binding hasn't completed, so Gdk/Gtk were also in blocking.


%package -n golang-github-linuxdeepin-go-gir-generator
Summary:        Additional mobile libraries
Group:          Development/Languages/Golang

BuildRequires:  golang
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gdk-2.0)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
Requires:       pkgconfig(gobject-introspection-1.0)
Requires:       pkgconfig(gudev-1.0)
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(gobject-2.0)
Requires:       pkgconfig(gio-2.0)
Requires:       pkgconfig(gdk-2.0)
Requires:       pkgconfig(gdk-3.0)
Requires:       pkgconfig(gudev-1.0)
Provides:       golang(github.com/linuxdeepin/go-gir/glib-2.0)
Provides:       golang(github.com/linuxdeepin/go-gir/gio-2.0)
Provides:       golang(github.com/linuxdeepin/go-gir/gobject-2.0)
Provides:       golang(github.com/linuxdeepin/go-gir/gudev-1.0)
BuildArch:      noarch

%description -n golang-github-linuxdeepin-go-gir-generator
Go-gir-generator imeplement static golang bindings for GObject.

There has many go bindings for GObject/Gtk libraries, but almost all of them 
are written by hand. It's bored and error-prone when the binding C libaray 
changed.

Go-gir-geneator's object is like python-gobject's that binding the newest 
library without need change binding codes.

Currently it only official support Gobject-2.0, Glib-2.0, Gio-2.0. Because 
generate the gdkpixbuf binding hasn't completed, so Gdk/Gtk were also in blocking.

%prep
%autosetup -p1 -n %{_name}-%{version}
	
sed -i "s/'Can'tFind'/“Can'tFind”/" lib.in/glib-2.0/keyfile_test.go
%build
#export GO111MODULE=off
#export CGO_ENABLED=1
#goprep %{import_path}
#gobuild ...
#go build
export GOPATH="%{gopath}"
%make_build

%install
go install

install -m 0644 gio-2.0/gio.gen.c %{buildroot}%{go_contribsrcdir}/%{import_path}/gio-2.0
install -m 0644 glib-2.0/glib.gen.c %{buildroot}%{go_contribsrcdir}/%{import_path}/glib-2.0
install -m 0644 gobject-2.0/fix_gobject.c %{buildroot}%{go_contribsrcdir}/%{import_path}/gobject-2.0
install -m 0644 gobject-2.0/gobject.gen.c %{buildroot}%{go_contribsrcdir}/%{import_path}/gobject-2.0
install -m 0644 gudev-1.0/gudev.gen.c %{buildroot}%{go_contribsrcdir}/%{import_path}/gudev-1.0

mv %{buildroot}%{_bindir}/generator %{buildroot}%{_bindir}/gir-generator
mv %{buildroot}%{_bindir}/test %{buildroot}%{_bindir}/gir-test
%fdupes %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md documentation/WhyWaf.txt documentation/Design.txt
%license LICENSE
%{_bindir}/gir-generator
%{_bindir}/gir-test

%files -n golang-github-linuxdeepin-go-gir-generator
%defattr(-,root,root,-)
%{go_contribsrcdir}/*
