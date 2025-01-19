Name:           libstrophe
Version:        0.13.1
Release:        4%{?dist}
Summary:        An XMPP library for C

# Automatically converted from old format: MIT and GPLv3 - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND GPL-3.0-only
URL:            https://strophe.im/%{name}/
Source0:        https://github.com/strophe/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  zlib-devel
# expat or libxml, but no need for both
BuildRequires:  expat-devel
#BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
# For docs
BuildRequires:  doxygen
BuildRequires:  lcov

%description
libstrophe is a minimal XMPP library written in C. It has almost no
external dependencies, only an XML parsing library (expat or libxml
are both supported). It is designed for both POSIX and Windows
systems.



%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.



%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
The %{name}-doc package contains HTML documentation for developing
applications that use %{name}.



%prep
%autosetup


%build
autoreconf -i -W all
# expat is the default; use --with-libxml2 to switch
# create a code coverage report: --enable-coverage
%configure --disable-static --enable-coverage
%make_build
# Build HTML documentation
doxygen
make coverage  # results are in coverage/


%install
%make_install
# Removing libstrophe.la generated
rm -f %{buildroot}%{_libdir}/libstrophe.la

# Install examples/ dir shipping binary files generated
mkdir -p %{buildroot}%{_libdir}/%{name}/
cp -a examples/ %{buildroot}%{_libdir}/%{name}/
mv %{buildroot}%{_libdir}/%{name}/examples/.libs %{buildroot}%{_libdir}/%{name}/examples/libs
mv %{buildroot}%{_libdir}/%{name}/examples/.deps %{buildroot}%{_libdir}/%{name}/examples/deps
rm -f %{buildroot}%{_libdir}/%{name}/examples/.dirstamp
rm -f %{buildroot}%{_libdir}/%{name}/examples/deps/.dirstamp

# Install HTML documentation for the doc subpackage
mkdir -p %{buildroot}%{_pkgdocdir}/
cp -a docs/html/ %{buildroot}%{_pkgdocdir}/
cp -a coverage/ %{buildroot}%{_pkgdocdir}/html/


%check
# the tests suite is launched with 'make coverage'
# no need to run it twice



%files
%license LICENSE.txt GPL-LICENSE.txt MIT-LICENSE.txt
%doc README AUTHORS ChangeLog 
%{_libdir}/%{name}.so.*


%files devel
%doc examples/README.md
%{_includedir}/strophe.h
%{_libdir}/%{name}.so
%{_libdir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc


%files doc
%{_pkgdocdir}/html/



%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 2 2024 Miroslav Suchý <msuchy@redhat.com> - 0.13.1-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 24 2024 Matthieu Saulnier <fantom@fedoraproject.org> - 0.13.1-1
- Update to 0.13.1

* Sat Feb 3 2024 Matthieu Saulnier <fantom@fedoraproject.org> - 0.13.0-2
- Add zlib as new BuildRequires

* Thu Feb 1 2024 Matthieu Saulnier <fantom@fedoraproject.org> - 0.13.0-1
- Update to 0.13.0
- Remove tests suite from devel subpackage
- Enable code coverage report
- Cleanup %%check section

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 2 2023 Matthieu Saulnier <fantom@fedoraproject.org> - 0.12.3-1
- Update to 0.12.3
- Improve file ownership in doc subpackage

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 26 2022 Matthieu Saulnier <fantom@fedoraproject.org> - 0.12.2-1
- Update to 0.12.2 version

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.10.1-5
- Rebuilt with OpenSSL 3.0.0

* Wed Aug 25 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.10.1-4
- Package Review RHBZ#1994501:
  - Remove useless ldconfig scriptlets
  - Fix Requires tag of the doc subpackage

* Thu Aug 19 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.10.1-3
- Package Review RHBZ#1994501:
  - Use more %%{name} macro in %%files section

* Tue Aug 17 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.10.1-2
- Package Review RHBZ#1994501:
  - Fix Requires tag of the doc subpackage

* Tue Aug 17 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.10.1-1
- Initial packaging
