Name:           libstrophe
Version:        0.14.0
Release:        2%{?dist}
Summary:        An XMPP library for C

License:        MIT AND GPL-3.0-only
URL:            https://strophe.im/%{name}/
Source0:        https://github.com/strophe/libstrophe/releases/download/%{version}/libstrophe-%{version}.tar.gz
Source1:        https://github.com/strophe/libstrophe/releases/download/%{version}/libstrophe-%{version}.tar.gz.asc
# https://github.com/strophe/libstrophe/issues/253
Patch:          C23.patch
# https://keys.openpgp.org/search?q=F8ADC1F9A68A7AFF0E2C89E4391A5EFC2D1709DE
Source2:        F8ADC1F9A68A7AFF0E2C89E4391A5EFC2D1709DE.asc

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
BuildRequires:  texinfo
# For signature verification
BuildRequires:  gpgverify

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

%description    doc
The %{name}-doc package contains docbook documentation for developing
applications that use %{name}.



%prep
%autosetup -p1
sed -i "s/GENERATE_DOCBOOK       = NO/GENERATE_DOCBOOK       = YES/g" Doxyfile
sed -i "s/GENERATE_HTML          = YES/GENERATE_HTML          = NO/g" Doxyfile

%build
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
autoreconf -i -W all
# expat is the default; use --with-libxml2 to switch
%configure --disable-static
%make_build
# Build docbook documentation
doxygen

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

# Install docbook documentation for the doc subpackage
mkdir -p %{buildroot}%{_datadir}/help/en/libstrophe
for file in docs/docbook/*.xml
do
  install -m644 ${file} %{buildroot}%{_datadir}/help/en/libstrophe/
done

%check
make check


%files
%license LICENSE.txt
%license GPL-LICENSE.txt
%license MIT-LICENSE.txt
%doc README
%doc AUTHORS
%doc ChangeLog 
%{_libdir}/%{name}.so.0*


%files devel
%doc examples/README.md
%{_includedir}/strophe.h
%{_libdir}/%{name}.so
%{_libdir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc


%files doc
%license LICENSE.txt
%license GPL-LICENSE.txt
%license MIT-LICENSE.txt
%dir %{_datadir}/help/en
%lang(en) %{_datadir}/help/en/libstrophe


%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri May 16 2025 Benson Muite <fed500@fedoraproject.org> - 0.14.0-1
- Update to 0.14.0 bz#2352379
- Use docbook for documentation

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
