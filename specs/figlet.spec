%global commit0 a565ae1e8f8254044219260dda2a6b51984930dc
%global date 20151018
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:       figlet
Summary:    A program for making large letters out of ordinary text
Version:    2.2.5
Release:    31%{?shortcommit0:.%{date}git%{shortcommit0}}%{?dist}
# Automatically converted from old format: BSD and MIT - review is highly recommended.
License:    LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:        http://www.figlet.org/

# Source repository at https://github.com/cmatsuoka/figlet
Source0:    https://github.com/cmatsuoka/%{name}/archive/%{commit0}/%{name}-%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  gcc
BuildRequires: make
%description
FIGlet prints its input using large characters (called "FIGcharacters") made
up of ordinary screen characters (called "sub-characters"). FIGlet output is
generally reminiscent of the sort of "signatures" many people like to put at
the end of e-mail and UseNet messages. It is also reminiscent of the output of
some banner programs, although it is oriented normally, not sideways.

%prep
%setup -q -n %{name}-%{commit0}

sed -i \
    -e 's|usr/local|usr|g' \
    -e 's|$(prefix)/man|$(prefix)/share/man|g' \
    Makefile

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%check
make check

%install
%make_install

%files
%license LICENSE
%doc CHANGES README FAQ
%{_mandir}/man6/*
%{_bindir}/*
%{_datadir}/%{name}/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-31.20151018gita565ae1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.5-30.20151018gita565ae1
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-29.20151018gita565ae1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-28.20151018gita565ae1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-27.20151018gita565ae1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-26.20151018gita565ae1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-25.20151018gita565ae1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-24.20151018gita565ae1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-23.20151018gita565ae1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-22.20151018gita565ae1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-21.20151018gita565ae1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-20.20151018gita565ae1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-19.20151018gita565ae1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-18.20151018gita565ae1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-17.20151018gita565ae1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-16.20151018gita565ae1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-15.20151018gita565ae1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-14.20151018gita565ae1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-13.20151018gita565ae1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 05 2017 Simone Caronni <negativo17@gmail.com> - 2.2.5-12.20151018gita565ae1
- Remove RHEL/CentOS 5 compatibility, clean up SPEC file.
- Use latest git snapshot (2015).

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 11 2015 Simone Caronni <negativo17@gmail.com> - 2.2.5-9
- Add additional patches from upstream

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 25 2015 Simone Caronni <negativo17@gmail.com> - 2.2.5-7
- Add license macro.
- Add upstream patches.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Simone Caronni <negativo17@gmail.com> - 2.2.5-1
- Updated to 2.2.5.

* Mon May 21 2012 Simone Caronni <negativo17@gmail.com> - 2.2.4-7
- Removed ms-dos fonts.
- Added check.
- Replace make macro with actual command.
- Added compile flags to make command.

* Mon May 14 2012 Simone Caronni <negativo17@gmail.com> - 2.2.4-6
- Review fixes.
- Removed contributed fonts as per review.

* Thu May 10 2012 Simone Caronni <negativo17@gmail.com> - 2.2.4-5
- Small changes.

* Wed Oct 26 2011 Simone Caronni <negativo17@gmail.com> - 2.2.4-4
- rpmlint fixes.

* Fri Oct 21 2011 Simone Caronni <negativo17@gmail.com> - 2.2.4-3
- Updated.
- Added additional fonts, reworked setup.

* Wed Nov 29 2006 Simone Caronni <slaanesh@fastwebnet.it> - 2.2.2-1.sla
- First build 
