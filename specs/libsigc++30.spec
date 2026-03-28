Name:           libsigc++30
Version:        3.8.0
Release:        %autorelease
Summary:        Typesafe signal framework for C++

License:        LGPL-2.1-or-later
URL:            https://github.com/libsigcplusplus/libsigcplusplus
Source0:        https://github.com/libsigcplusplus/libsigcplusplus/releases/download/%{version}/libsigc++-%{version}.tar.xz

BuildRequires:  docbook-style-xsl
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libxslt
BuildRequires:  m4
BuildRequires:  meson
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl-interpreter

%description
libsigc++ implements a typesafe callback system for standard C++. It
allows you to define signals and to connect those signals to any
callback function, either global or a member function, regardless of
whether it is static or virtual.

libsigc++ is used by gtkmm to wrap the GTK+ signal system. It does not
depend on GTK+ or gtkmm.


%package        devel
Summary:        Development tools for the typesafe signal framework for C++
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains the static libraries and header files
needed for development with %{name}.


%package        doc
Summary:        Documentation for %{name}, includes full API docs
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains the full API documentation for %{name}.


%prep
%autosetup -n libsigc++-%{version}

chmod -x NEWS


%build
%meson -Dbuild-documentation=true
%meson_build


%install
%meson_install


%files
%license COPYING
%doc NEWS README.md
%{_libdir}/libsigc-3.0.so.0*

%files devel
%{_includedir}/sigc++-3.0/
%{_libdir}/sigc++-3.0/
%{_libdir}/pkgconfig/sigc++-3.0.pc
%{_libdir}/libsigc-3.0.so

%files doc
%doc %{_datadir}/doc/libsigc++-3.0/
%doc %{_datadir}/devhelp/


%changelog
%autochangelog
