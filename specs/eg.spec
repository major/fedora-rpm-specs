Name:           eg
Version:        1.7.5.2
Release:        41%{?dist}
Summary:        Git for mere mortals
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://www.gnome.org/~newren/eg/
Source0:        %{name}-%{version}.tar.gz
Patch0:		eg-1.7.5.2-fix-use-false-detection.patch
# To reproduce, run:
# git clone git://gitorious.org/eg/mainline.git eg
# cd eg
# git archive --format=tar --prefix=eg-1.7.5.2/ v1.7.5.2 | gzip > eg-1.7.5.2.tar.gz
BuildRequires:  bash-completion
BuildRequires:	perl-generators
Requires:       perl-interpreter
BuildArch:      noarch
Requires:       git

%description
Easy Git (eg) is a wrapper for git, designed to make git easy to learn and use.

%prep
%setup -q
%patch -P0 -p1 -b .false

# Filter unwanted Requires:
cat << \EOF > %{name}-prov
#!/bin/sh
%{__perl_requires} $* |\
  sed -e '/perl(the)/d;/perl(an)/d;/perl(it)/d;/perl(one)/d'
EOF

%define __perl_requires %{_builddir}/%{name}-%{version}/%{name}-prov
chmod +x %{__perl_requires}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
install -m 755 eg $RPM_BUILD_ROOT/%{_bindir}/

bashcompdir=$(pkg-config --variable=completionsdir bash-completion || :)
if [ "$bashcompdir" ]; then
    install -Dpm 644 bash-completion-eg.sh $RPM_BUILD_ROOT$bashcompdir/eg
    echo %{_datadir}/bash-completion > %{name}.files
else
    install -Dpm 644 bash-completion-eg.sh \
        $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/eg
    echo %{_sysconfdir}/bash_completion.d > %{name}.files
fi

%files -f %{name}.files
%doc README
%{_bindir}/eg

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.5.2-40
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.5.2-33
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.5.2-30
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.5.2-27
- Perl 5.32 re-rebuild of bootstrapped packages

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.5.2-26
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.5.2-23
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.5.2-20
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 21 2017 Ville Skyttä <ville.skytta@iki.fi> - 1.7.5.2-18
- Install bash completion to where bash-completion.pc says

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 1.7.5.2-16
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.5.2-15
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.5.2-13
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.5.2-10
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.5.2-9
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.7.5.2-6
- Perl 5.18 rebuild

* Tue Apr 30 2013 Tom Callaway <spot@fedoraproject.org> - 1.7.5.2-5
- patch out false "use " cases, where the word "use" appears at the beginning
  of a block of documentation text (we strip these out anyways, but this patch can go upstream)

* Tue Apr 23 2013 Luis Bazan <lbazan@fedoraproject.org> - 1.7.5.2-4
- add other one requires

* Tue Apr 23 2013 Luis Bazan <lbazan@fedoraproject.org> - 1.7.5.2-3
- add requires

* Mon Apr 22 2013 Luis Bazan <lbazan@fedoraproject.org> - 1.7.5.2-2
- add dependecys

* Mon Apr 08 2013 Luis Bazan <lbazan@fedoraproject.org> - 1.7.5.2-1
- New Upstream Version
- change instructions to clone the new version

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 05 2012 Luis Bazan <bazanluis20@gmail.com> 1.7.3-8
- repair version to eg-1.7.3 
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 09 2009 James Bowes <jbowes@redhat.com> 0.97-3
- Filter out more spurious requires

* Sun Feb 08 2009 James Bowes <jbowes@redhat.com> 0.97-2
- Version bump for koji

* Sun Feb 08 2009 James Bowes <jbowes@redhat.com> 0.97-1
- Update to 0.97

* Thu Apr 17 2008 James Bowes <jbowes@redhat.com> 0.70-2
- Filter out the requires 'perl(the)'

* Thu Apr 17 2008 James Bowes <jbowes@redhat.com> 0.70-1
- Initial packaging for Fedora
