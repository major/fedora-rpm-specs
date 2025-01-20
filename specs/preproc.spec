# vim: syntax=spec

%if 0%{?fedora} || 0%{?rhel} > 7
%global python_pkg python3
%global python /usr/bin/python3
%else
%global python_pkg python2
%global python /usr/bin/python2
%endif

Name: preproc
Version: 0.5
Release: 13%{?dist}
Summary: Simple text preprocessor
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://pagure.io/rpkg-util.git

%if 0%{?fedora} || 0%{?rhel} > 6
VCS: git+ssh://git@pagure.io/rpkg-util.git#bcad4393160b3fe9f624ebdc0ac1a65dffd75754:preproc
%endif

# Source is created by:
# git clone https://pagure.io/rpkg-util.git
# cd rpkg-util/preproc
# git checkout preproc-0.5-1
# ./rpkg spec --sources
Source0: rpkg-util-preproc-bcad4393.tar.gz

# Upstream indicates non-maintenance (aside from security) and 3.11 in F37 deprecates the
# pipes module (it's been deprecated since 2.7?).
Patch0: 0001-pipes-to-shlex.patch

BuildArch: noarch

BuildRequires: %{python_pkg}
Requires: %{python_pkg}

%if 0%{?rhel} == 6
BuildRequires: python-argparse
Requires:      python-argparse
%endif

%description
Simple text preprocessor implementing a very basic templating language.
You can use bash code enclosed in triple braces in a text file and
then pipe content of that file to preproc. preproc will replace each of
the tags with stdout of the executed code and print the final renderred
result to its own stdout.

%prep
%setup -T -b 0 -q -n rpkg-util-preproc
%patch -P0 -p1

%check
sed -i '1 s|#.*|#!%{python}|' preproc
./test

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 preproc %{buildroot}%{_bindir}

sed -i '1 s|#.*|#!%{python}|' %{buildroot}%{_bindir}/preproc

install -d %{buildroot}%{_mandir}/man1
install -p -m 0644 man/preproc.1 %{buildroot}%{_mandir}/man1

%files
%{!?_licensedir:%global license %doc}
%license LICENSE
%{_bindir}/preproc
%{_mandir}/man1/preproc.1*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Aug 6 2022 Simon de Vlieger <cmdr@supakeen.com> - 0.5-6
- Patch `pipes` DeprecationWarning (makes dependents ftbfs)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 clime <clime@fedoraproject.org> 0.5-1
- we need to sed python version also in %%check section of spec

* Sat Jan 16 2021 clime <clime@fedoraproject.org> 0.4-1
- fix tests, add correct requires and buildrequires

* Sun Jan 03 2021 clime <clime@fedoraproject.org> 0.3-1
- test preproc when building

* Tue Mar 10 2020 clime <clime@fedoraproject.org> 0.2-1
- encoding fixes
- make regular-expression only implementation
- add NOTE into help/man about usage of preproc on uknown files

* Tue Mar 03 2020 clime <clime@fedoraproject.org> 0.1-1
- use cmd_repr helper to properly render the executed command
- strip starting and ending whitespaces if any
- change to working email
- pass now required path to git_vcs macro in spec file
- source env before sourcing anything else
- fix spec files after CACHE to OUTPUT rename
- fix rpkg-util spec files
- build fix for rhel6
- provide man pages statically and add regen.sh
- add some explanation for tags matching
- allow multiple lines inside {{{}}}, fix expression for quoted
strings so that the closest quote is matched
- add missing BRs
- move preproc and rpkg macro defs into separate packages
