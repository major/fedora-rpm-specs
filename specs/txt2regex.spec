Name:           txt2regex
Version:        0.9
Release:        13%{?dist}
Summary:        Regular expression wizard that converts human sentences to regexes

License:        GPL-2.0-only
URL:            https://aurelio.net/projects/txt2regex/
Source0:        https://github.com/aureliojargas/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# This removes the "TEXTDOMAINDIR=..." line from txt2regex. It isn't needed in
# Fedora where the default value is OK.
Patch0:         txt2regex-no-TEXTDOMAINDIR.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  gettext
Requires:       bash >= 3.0

%description
txt2regex is a regular expression wizard that converts human sentences to
regexes.

In a simple interactive interface, you just answer questions and build your
own regex for a large variety of software and programming languages.

%prep
%setup -q
%patch -P0 -p1

%build
# nothing to do

%install

# install txt2regex and locale files
make DESTDIR=%{buildroot} install

# install man page
mkdir -p %{buildroot}/%{_mandir}/man1
install -p -m 644 man/txt2regex.man %{buildroot}%{_mandir}/man1/txt2regex.1

# find locale files
%find_lang %{name}

%files -f %{name}.lang
%doc CHANGELOG.md CONTRIBUTING.md README.md TODO
%license COPYRIGHT
%{_bindir}/txt2regex
%{_mandir}/man1/txt2regex.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Richard Fearn <richardfearn@gmail.com> - 0.9-9
- Don't glob everything under shared directories in %%files

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 27 2022 Richard Fearn <richardfearn@gmail.com> - 0.9-7
- Use SPDX license identifier

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Richard Fearn <richardfearn@gmail.com> 0.9-1
- Update to new upstream version 0.9 (#1838383)

* Sun Feb 02 2020 Richard Fearn <richardfearn@gmail.com> 0.8-23
- Use %%license

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 05 2019 Richard Fearn <richardfearn@gmail.com> 0.8-19
- Don't remove buildroot in %%install section

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 16 2017 Richard Fearn <richardfearn@gmail.com> 0.8-16
- Remove unnecessary Group: tag, BuildRoot: tag, and %%clean section

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 02 2016 Richard Fearn <richardfearn@gmail.com> 0.8-13
- Fix incorrect FSF address in COPYRIGHT

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Richard Fearn <richardfearn@gmail.com> 0.8-11
- Remove unnecessary %%defattr

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 18 2010 Richard Fearn <richardfearn@gmail.com> - 0.8-3
- include email confirming licence is GPLv2 only, as required by
  https://fedoraproject.org/wiki/Packaging:LicensingGuidelines

* Wed Jun  9 2010 Richard Fearn <richardfearn@gmail.com> - 0.8-2
- fix licence: upstream has confirmed that it should be GPLv2 only
- improve description
- use for loop to convert files to UTF-8

* Sun Jun  6 2010 Richard Fearn <richardfearn@gmail.com> - 0.8-1
- initial package for Fedora
