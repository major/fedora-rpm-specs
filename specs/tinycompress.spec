Name:          tinycompress
Version:       1.2.13
Release:       2%{?dist}
Summary:       A library for compress audio offload in alsa
# Automatically converted from old format: BSD and LGPLv2 - review is highly recommended.
License:       LicenseRef-Callaway-BSD AND LicenseRef-Callaway-LGPLv2
URL:           http://alsa-project.org/
Source0:       ftp://ftp.alsa-project.org/pub/tinycompress/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires: gcc

%description
tinycompress is a library for compress audio offload in alsa

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
Files for development with %{name}.

%package utils
Summary: Utilities for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Utilies for testing of compressed audio with %{name}.

%prep
%setup -q

%build
%configure --disable-static

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

#Remove libtool archives.
find %{buildroot} -name '*.la' -delete

%check
make check

%ldconfig_scriptlets

%files
%license COPYING
%doc README
%{_libdir}/*.so.*

%files devel
%{_includedir}/tinycompress*
%{_libdir}/*.so
%{_libdir}/pkgconfig/tinycompress.pc

%files utils
%{_bindir}/cplay
%{_bindir}/crecord

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 12 2024 Jaroslav Kysela <perex@perex.cz> 1.2.13-1
- 1.2.13 release

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.11-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Jaroslav Kysela <perex@perex.cz> 1.2.11-1
- 1.2.11 release

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 24 2022 Jaroslav Kysela <perex@perex.cz> 1.2.8-1
- 1.2.8 release

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 31 2021 Jaroslav Kysela <perex@perex.cz> 1.2.4-1
- 1.2.5 release

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 20 2020 Jaroslav Kysela <perex@perex.cz> 1.2.4-3
- 1.2.4 release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 19 2020 Jaroslav Kysela <perex@perex.cz> 1.2.2-1
- 1.2.2 release

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.7-1
- 1.1.7 release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr  8 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.6-1
- 1.1.6 release

* Fri Mar  9 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.5-3
- Add gcc BR

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 15 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.5-1
- 1.1.5 release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 17 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.4-1
- 1.1.4 release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.3-1
- 1.1.3 release

* Fri Apr  1 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.1-1
- 1.1.1 release

* Sat Feb 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.0-2
- Minor updates

* Fri Nov 13 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.0-1
- Initial package
