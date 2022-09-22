Name:           movit
Version:        1.6.3
Release:        6%{?dist}
Summary:        GPU video filter library
License:        GPLv2+
Url:            https://movit.sesse.net
Source0:        https://movit.sesse.net/%{name}-%{version}.tar.gz
Source1:        COPYING
Patch0:         gcc_erase_signature.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(sdl2)
%if ! (0%{?rhel} >= 8)
BuildRequires:  pkgconfig(SDL2_image)
%endif
BuildRequires:  gtest-devel
Requires:       %{name}-data = %{version}-%{release}

%description
Movit is a library for video filters. It uses the GPU present in many
computers to accelerate computation of common filters and
transitions, facilitating real-time HD video editing.

This package contains the Movit shared library.

%package devel
Summary:        Development files for the Movit GPU video filter library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Movit is a library for video filters. It uses the GPU present in many
computers to accelerate computation of common filters and
transitions, facilitating real-time HD video editing.

This package contains the development files (library and header files).

%package        data
Summary:        Data files for the Movit GPU video filter library
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    data
Movit is a library for video filters. It uses the GPU present in many
computers to accelerate computation of common filters and
transitions, facilitating real-time HD video editing.

This package contains the architecture-independent data files.

%prep
%setup -q
cp -a %{SOURCE1} .
%if 0%{?rhel} && 0%{?rhel} < 8
%patch0 -p1
%endif

%build
%configure --disable-static
%make_build TESTS=

%install
sed -i 's/-m 0644 libmovit.la/libmovit.la/' Makefile
%make_install

rm %{buildroot}%{_libdir}/libmovit.la

#check
# skipped test suite due src/gtest-all.cc is missing
# make check

%ldconfig_scriptlets

%files
%doc README NEWS
%license COPYING
%{_libdir}/libmovit.so.*

%files data
%{_datadir}/movit/

%files devel
%{_libdir}/libmovit.so
%{_includedir}/movit/
%{_libdir}/pkgconfig/movit.pc

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 31 2021 Jonathan Wakely <jwakely@redhat.com> - 1.6.3-3
- Rebuilt for removed libstdc++ symbols (#1937698)

* Fri Mar 05 2021 Sérgio Basto <sergio@serjux.com> - 1.6.3-2
- Fix build on epel7

* Thu Feb 18 2021 Sérgio Basto <sergio@serjux.com> - 1.6.3-1
- Update movit to 1.6.3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 12 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.6.2-1
- Update to 1.6.2

* Fri Feb 23 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.6.1-1
- Update to 1.6.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0
- Add pkgconfig(sdl2)
- Add pkgconfig(SDL2_image)

* Sat Sep 23 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.5.3-2
- Correct license tag to GPLv2+
- Add comment why adding licensing test file
- Add %%license macro only to main package
- Add RR %%{name}-data = %%{version}-%%{release} to main package
- Add RR %%{name} = %%{version}-%%{release} to data sub package

* Sat Sep 09 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.5.3-1
- Initial package: movit-1.5.3
