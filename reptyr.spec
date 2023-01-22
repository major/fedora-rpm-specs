%global commit0 f2a60ce3f9ac3a96140472cd1e1e71a448d42293
Name:           reptyr
Version:        0.9.0
Release:        3%{?dist}
Summary:        Attach a running process to a new terminal

License:        MIT
URL:            http://github.com/nelhage/reptyr
Source0:        https://github.com/nelhage/reptyr/archive/%{name}-%{version}.tar.gz
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64
BuildRequires: make
Requires: pkgconf-pkg-config
BuildRequires:  gcc
BuildRequires:  %{_bindir}/python3
BuildRequires:  python3-pexpect
# https://github.com/nelhage/reptyr/issues/69
BuildRequires:  kernel-headers >= 3.4

%description
reptyr is a utility for taking an existing running program and
attaching it to a new terminal.  Started a long-running process over
ssh, but have to leave and don't want to interrupt it?  Just start a
screen, use reptyr to grab it, and then kill the ssh session and head
on home.


%prep
%setup -q -n %{name}-%{name}-%{version}
sed -i s/python2/python3/g Makefile

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX="%{_prefix}" DESTDIR="$RPM_BUILD_ROOT"
%find_lang %{name} --with-man


%check
make test CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"


%files -f %{name}.lang
%define bashcomp %(pkg-config --variable=completionsdir bash-completion)
%if "%{bashcomp}" == "%{nil}"
%define bashcomp /etc/bash_completion.d
%endif

%{!?_licensedir:%global license %%doc}
%license COPYING
%doc ChangeLog NOTES README.md
%{_bindir}/reptyr
%{_mandir}/man1/reptyr.1*
%{bashcomp}/reptyr

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Francisco Javier Tsao Santín <tsao@disroot.org> - 0.9.0-1
- Upgrade to 0.9.0 version

* Wed Mar 23 2022 Francisco Javier Tsao Santín <tsao@disroot.org> - 0.8.0-5
- Removed no longer needed conditionals on testing (fixes EPEL9 build)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Francisco Javier Tsao Santín <tsao@disroot.org> - 0.8.0-1
- Upgraded to 0.8.0 (#1883748)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 7 2019 Francisco Javier Tsao Santín <tsao@gpul.org> - 0.7.0-1
- Upgraded to 0.7.0 (#1744587)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Francisco Javier Tsao Santín <tsao@gpul.org> - 0.6.2-13
- Upgraded to PR 91 (fix previous issues, add python3 support in tests and bash completion file)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.2-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Feb 19 2018 Francisco Javier Tsao Santín <tsao@gpul.org> - 0.6.2-10
- Added gcc to build requirements

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 20 2017 Ville Skyttä <ville.skytta@iki.fi> - 0.6.2-6
- Apply upstream gcc7 build fixes (#1424256)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Ville Skyttä <ville.skytta@iki.fi> - 0.6.2-3
- Remove unnecessary %%defattr
- Disable tests on EL (python-pexpect N/A, too old kernel-headers on 5 and 6)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Feb  1 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.6.2-1
- Update to 0.6.2

* Wed Jan 21 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.6.1-1
- Update to 0.6.1
- Mark license files as %%license where available

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 10 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.5-1
- Update to 0.5.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Aug 26 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.4-1
- Update to 0.4.
- Link with $RPM_LD_FLAGS.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat May 28 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.3-1
- Update to 0.3.

* Fri Mar 11 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.2-2.20110311git919fff7
- Update to git revision 919fff7, fixes crash with invalid arguments.

* Sat Mar  5 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.2-1
- First build.
