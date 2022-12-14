Summary: A Bayesian spam filter
Name: spamprobe
# upstream uses letters for patch version numbers
Version: 1.4d
Release: 26%{?dist}

Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Compile fixes for EL6, F16, F17 -- Tracker 3557020
Patch0: compile-fixes.patch
# 64bit hash support -- Tracker 2998863
Patch1: 64bit.patch
# example swapped -- Tracker 1856880
Patch2: example-swapped.patch
Patch3: spamprobe-gcc11.patch
Patch4: spamprobe-libpng.patch
Patch5: spamprobe-configure-c99.patch

License: QPL
URL: http://spamprobe.sourceforge.net/
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires: libdb-devel

%description
A spam filter that takes a different approach from the typical 
hand crafted rules based systems.  Instead of using pattern matching
and a set of human generated rules SpamProbe relies on a Bayesian
analysis of the frequency of words used in spam and non-spam emails
received by an individual person.  The process is completely automatic
and tailors itself to the kinds of emails that each person receives.
Spamprobe is not a mail filtering program itself but is designed to
plug into another mail filtering system like procmail or
Perl Mail::Procmail.

%prep
%setup -q
%patch0 -p1 -b .compile-fixes
%patch1 -p1 -b .64bit
%patch2 -p1 -b .examples-swapped
%patch3 -p1 -b .gcc11
%patch4 -p1 -b .libpng
%patch5 -p1 -b .c99

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%files
%doc README.txt LICENSE.txt ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Mon Dec 12 2022 Florian Weimer <fweimer@redhat.com> - 1.4d-26
- Port configure script to C99

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4d-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4d-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4d-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4d-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 Jeff Law <law@redhat.com> - 1.4d-20
- Make comparison functions invocable as const
- Deal with libpng removing a couple symbols

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4d-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4d-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4d-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4d-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4d-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4d-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4d-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4d-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4d-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4d-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4d-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4d-8
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4d-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4d-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4d-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4d-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Aug 26 2012 Steven Roberts <strobert@strobe.net> 1.4d-3
- changed sourceforge download link

* Sat Aug 25 2012 Steven Roberts <strobert@strobe.net> 1.4d-2
- drop prefix -- no longer relocatable to meet Fedora project guidelines
- switched from using %%makeinstall
- drop explicit Requires.  let build process determine them
- Added URL field (rpmlint tagged it missing)
- handle db4 -> libdb change with fedora >= 18
- Compile fixes for EL6, F16, F17 - Tracker 3557020
- added patch for 64bit hash support - Tracker 2998863
- README.txt had example swapped - Tracker 1856880

* Wed Jan 28 2009 Steven Roberts <strobert@strobe.net> 1.4d-1
- Initial packaging for EL 5
