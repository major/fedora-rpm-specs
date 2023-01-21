Name:           minimodem
Version:        0.24
Release:        15%{?dist}
Summary:        General-purpose software audio FSK modem

License:        GPLv3+
URL:            http://www.whence.com/minimodem/
Source0:        http://www.whence.com/minimodem/minimodem-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  fftw3-devel alsa-lib alsa-lib-devel libsndfile-devel pulseaudio-libs-devel
Requires:       fftw

%description
Minimodem is a command-line program which decodes (or generates) audio modem
tones at any specified baud rate, using various framing protocols. It acts a
general-purpose software FSK modem, and includes support for various standard
FSK protocols such as Bell103, Bell202, RTTY, NOAA SAME, and Caller-ID.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%check
cd tests
make check-TESTS

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%doc AUTHORS ChangeLog COPYING NEWS README THANKS 

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 21 2016 Ricky Elrod <relrod@redhat.com> - 0.24-1
- Latest upstream release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 24 2015 Ricky Elrod <relrod@redhat.com> - 0.22.1-1
- Latest upstream release.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 14 2014 Ricky Elrod <relrod@redhat.com> - 0.20-1
- Latest upstream release.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 2 2013 Jimmy Carter <kg4sgp@gmail.com> - 0.19-2
- Rebuilding.

* Wed Oct 2 2013 Jimmy Carter <kg4sgp@gmail.com> - 0.19-1
- Latest upstream release.

* Wed Sep 18 2013 Jimmy Carter <kg4sgp@gmail.com> - 0.18-1
- Latest upstream release.
- Running tests.
- Added docs.

* Wed Apr 17 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.17.1-2
- Enable sndfile and pulseaudio in build.

* Tue Apr 2 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.17.1-1
- Initial build.

