Name:           httpie
Version:        3.2.2
Release:        4%{?dist}
Summary:        A Curl-like tool for humans

License:        BSD-3-Clause
URL:            https://httpie.org/
Source:         https://github.com/httpie/httpie/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

# The tests are enabled by default, --without tests option exists
%bcond_without tests

%description
HTTPie is a CLI HTTP utility built out of frustration with existing tools. The
goal is to make CLI interaction with HTTP-based services as human-friendly as
possible.

HTTPie does so by providing an http command that allows for issuing arbitrary
HTTP requests using a simple and natural syntax and displaying colorized
responses.


%prep
%autosetup -p1

# Upstream pins werkzeug<2.1.0 to avoid a problem in httpbin that Fedora has patch for
# https://github.com/httpie/httpie/pull/1345
# we revert it to allow building with newer werkzeug
sed -i "/'werkzeug<2.1.0'/d" setup.py


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x test}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files httpie

# Bash completion
mkdir -p %{buildroot}%{bash_completions_dir}
cp -a extras/httpie-completion.bash %{buildroot}%{bash_completions_dir}/http
ln -s ./http %{buildroot}%{bash_completions_dir}/https

# Fish completion
mkdir -p %{buildroot}%{fish_completions_dir}/
cp -a extras/httpie-completion.fish %{buildroot}%{fish_completions_dir}/http.fish
ln -s ./http.fish %{buildroot}%{fish_completions_dir}/https.fish

# Man pages
mkdir -p %{buildroot}%{_mandir}/man1
cp -a extras/man/*.1 %{buildroot}%{_mandir}/man1/


%check
%if %{with tests}
# Werkzeug >= 3 failures
# https://github.com/httpie/cli/issues/1530
%pytest -v -k "not test_compress_form and not test_binary"
%else
%pyproject_check_import
%endif


%files -f %{pyproject_files}
%doc README.md
%{_bindir}/http
%{_bindir}/https
%{_bindir}/httpie
%{_mandir}/man1/http.1*
%{_mandir}/man1/https.1*
%{_mandir}/man1/httpie.1*
%{bash_completions_dir}/http
%{bash_completions_dir}/https
%{fish_completions_dir}/http.fish
%{fish_completions_dir}/https.fish


%changelog
* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Frantisek Zatloukal <fzatlouk@redhat.com> - 3.2.2-3
- Deselect tests failing with Werkzeug 3.x

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Miro Hrončok <mhroncok@redhat.com> - 3.2.2-1
- Update to 3.2.2
- Fixes: rhbz#2208673
- Fixes: rhbz#2171570

* Thu Jan 19 2023 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-5
- Don't explicitly require werkzeug<2.1.0 for tests

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.2.1-2
- Rebuilt for Python 3.11
- Fixes: rhbz#2094006

* Fri May 06 2022 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-1
- Update to 3.2.1
- Fixes: rhbz#2082447

* Thu May 05 2022 Miro Hrončok <mhroncok@redhat.com> - 3.2.0-2
- Install upstream manual pages instead of generating them

* Thu May 05 2022 Miro Hrončok <mhroncok@redhat.com> - 3.2.0-1
- Update to 3.2.0
- Fixes: rhbz#2082364

* Tue Mar 08 2022 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-1
- Update to 3.1.0
- Fixes: rhbz#2061597

* Mon Jan 24 2022 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-1
- Update to 3.0.2
- Fixes: rhbz#2044572

* Mon Jan 24 2022 Miro Hrončok <mhroncok@redhat.com> - 3.0.1-1
- Update to 3.0.1
- Fixes: rhbz#2044058

* Fri Jan 21 2022 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-1
- Update to 3.0.0
- Fixes: rhbz#2043680

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 15 2021 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-1
- Update to 2.6.0
- Fixes: rhbz#2014022

* Tue Sep 07 2021 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-1
- Update to 2.5.0
- Fixes: rhbz#2001693

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4.0-3
- Rebuilt for Python 3.10

* Thu May 27 2021 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-2
- Add Bash and Fish completion
- Fixes rhbz#1834441
- Run tests on build time

* Wed Mar 24 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.4.0-1
- Update to 2.4.0
- Use pypi_source macro

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Nils Philippsen <nils@tiptoe.de> - 2.3.0-2
- use macros for Python dependencies
- add missing Python dependencies needed for running help2man
- remove manual Python dependencies
- discard stderr when running help2man

* Thu Dec 24 2020 Nils Philippsen <nils@tiptoe.de> - 2.3.0-1
- version 2.3.0
- Python 2 is no more
- use %%autosetup and Python build macros
- remove EL7-isms
- explicitly require sed for building

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.3-3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 Rick Elrod <relrod@redhat.com> - 1.0.3-1
- Latest upstream

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-15
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-11
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 10 2017 Ralph Bean <rbean@redhat.com> - 0.9.4-8
- Fix help2man usage with python3.
  https://bugzilla.redhat.com/show_bug.cgi?id=1430733

* Mon Feb 27 2017 Ralph Bean <rbean@redhat.com> - 0.9.4-7
- Fix missing Requires.  https://bugzilla.redhat.com/show_bug.cgi?id=1417730

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 2 2017 Ricky Elrod <relrod@redhat.com> - 0.9.4-5
- Add missing Obsoletes.

* Mon Jan 2 2017 Ricky Elrod <relrod@redhat.com> - 0.9.4-4
- Nuke python-version-specific subpackages. Just use py3 if we can.

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jul 05 2016 Ricky Elrod <relrod@redhat.com> - 0.9.4-1
- Update to latest upstream.

* Fri Jun 03 2016 Ricky Elrod <relrod@redhat.com> - 0.9.3-4
- Add proper Obsoletes for rhbz#1329226.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 04 2016 Ralph Bean <rbean@redhat.com> - 0.9.3-2
- Modernize python macros and subpackaging.
- Move LICENSE to %%license macro.
- Make python3 the default on modern Fedora.

* Mon Jan 04 2016 Ralph Bean <rbean@redhat.com> - 0.9.3-1
- new version

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Ricky Elrod <relrod@redhat.com> - 0.9.2-1
- Latest upstream release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri Jan 31 2014 Ricky Elrod <codeblock@fedoraproject.org> - 0.8.0-1
- Latest upstream release.

* Fri Oct 4 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.7.2-2
- Add in patch to work without having python-requests 2.0.0.

* Sat Sep 28 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.7.2-1
- Latest upstream release.

* Thu Sep 5 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.6.0-7
- Only try building the manpage on Fedora, since RHEL's help2man doesn't
  have the --no-discard-stderr flag.

* Thu Sep 5 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.6.0-6
- Loosen the requirement on python-pygments.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 2 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.6.0-4
- python-requests 1.2.3 exists in rawhide now.

* Sun Jun 30 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.6.0-3
- Patch to use python-requests 1.1.0 for now.

* Sat Jun 29 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.6.0-2
- Update to latest upstream release.

* Mon Apr 29 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.5.0-2
- Fix changelog messup.

* Mon Apr 29 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.5.0-1
- Update to latest upstream release.

* Mon Apr 8 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.4.1-3
- Fix manpage generation by exporting PYTHONPATH.

* Tue Mar 26 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.4.1-2
- Include Python3 support, and fix other review blockers.

* Mon Mar 11 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.4.1-1
- Update to latest upstream release

* Thu Jul 19 2012 Ricky Elrod <codeblock@fedoraproject.org> - 0.2.5-1
- Initial build.
