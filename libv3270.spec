%bcond_without docs

Name:           libv3270
Version:        5.4
Release:        4%{?dist}
Summary:        3270 Virtual Terminal for GTK+3

License:        LGPLv3
URL:            https://github.com/PerryWerneck/libv3270
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gettext-devel
BuildRequires:  gtk3-devel
BuildRequires:  lib3270-devel
%if %{with docs}
BuildRequires:  doxygen
BuildRequires:  graphviz
%endif

%description
Originally designed as part of the pw3270 application, this library provides a
TN3270 virtual terminal widget for GTK+3.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gtk3-devel%{?_isa}
Requires:       lib3270-devel%{?_isa}
Requires:       glade-libs%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{with docs}
%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for %{name}.
%endif

%prep
%autosetup

%build
NOCONFIGURE=1 ./autogen.sh
%configure
# override SHELL to make the build more verbose
%make_build all SHELL='sh -x'
%if %{with docs}
doxygen doxygen
%endif

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%doc README.md AUTHORS
%{_libdir}/%{name}.so.5*
%{_datadir}/pw3270/colors.conf
%{_datadir}/pw3270/remap

%files devel
%{_datadir}/glade/catalogs/v3270.xml
%{_datadir}/glade/pixmaps/hicolor/*/actions/*.png
%{_datadir}/pw3270/pot/%{name}.pot
%{_includedir}/v3270.h
%{_includedir}/v3270
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*.pc

%if %{with docs}
%files doc
%license LICENSE
%doc html
%endif

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 23 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 5.4-1
- New upstream release

* Wed Mar 17 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 5.3-5
- Update requires for devel sub-package

* Wed Mar 17 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 5.3-4
- Update build requires
- Stricter globbing for library soname

* Sat Mar 13 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 5.3-3
- Add license to doc sub-package and make it noarch
- Update URL

* Sat Mar 13 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 5.3-2
- Do not remove buildroot on install
- Make build output more verbose
- Ensure build flags are applied
- Build docs

* Wed Mar  3 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 5.3-1
- Initial package
