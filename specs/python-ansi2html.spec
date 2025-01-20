# Run tests by default
%bcond_without tests

%global srcname ansi2html

Name:       python-%{srcname}
Version:    1.9.2
Release:    3%{?dist}
Summary:    Python module that converts text with ANSI color to HTML
# While the project was previously licensed as GPLv3+, it is now LGPLv3.
# See https://github.com/pycontribs/ansi2html/issues/72 and also
# https://github.com/pycontribs/ansi2html/issues/188 for more info.
# In these issues, all of the previous contributors agreed to relicense their code.
License:    LGPL-3.0-only
URL:        http://github.com/pycontribs/%{srcname}
Source:     %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  python3-devel
# Needed for building manpages
BuildRequires:  /usr/bin/a2x

%global _description %{expand:
The ansi2html module can convert text with ANSI color codes to HTML.}

%description %{_description}

%package -n python3-%{srcname}
Summary:    %{summary}
%dnl colorized-logs also provides %{_bindir}/ansi2html and %{_mandir}/man1/ansi2html.1*
Conflicts:  colorized-logs

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
# The -t is set if %%{with_tests} is true
%pyproject_buildrequires %{?with_tests:-t}

%build
# Build manpages
a2x \
    --conf-file=man/asciidoc.conf \
    --attribute="manual_package=ansi2html" \
    --attribute="manual_title=ansi2html Manual" \
    --attribute="manual_version=%{version}" \
    --format=manpage -D man \
     man/ansi2html.1.txt

# Build wheel
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

# Install manpage
install -Dpm 644 man/%{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1

%check
%if %{with tests}
%tox
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md docs/*.md
%license LICENSE
%{_bindir}/%{srcname}
%{_mandir}/man1/%{srcname}.1*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 05 2024 Federico Pellegrin <fede@evolware.org> - 1.9.2-1
- Upgrade to 1.9.2 (rhbz#2291612, rhbz#2248711, rhbz#2104976)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.8.0-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 07 2022 Maxwell G <gotmax@e.email> - 1.8.0-1
- Update to 1.8.0.

* Mon Jul 04 2022 Maxwell G <gotmax@e.email> - 1.7.0-1
- Update to 1.7.0.
- Resolves: rhbz#2103659.

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.6.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 21 2021 Maxwell G <gotmax@e.email> - 1.6.0-4
- gating.yml (3)

* Sun Dec 19 2021 Maxwell G <gotmax@e.email> - 1.6.0-3
- Fix gating.yml test names

* Sun Dec 19 2021 Maxwell G <gotmax@e.email> - 1.6.0-2
- Rebuild with fixed gating,yml

* Wed Nov 17 2021 Maxwell G <gotmax@e.email> - 1.6.0-1
- Update to 1.6.0. Fixes rhbz#1888556.
- Implement new Fedora Python Packaging Guidelines.
- Fix licensing
- Replace mock with unittests.mock and use tox.
- Use %%{srcname} globally
- Move to new upstream

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.1-12
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 02 2018 Ralph Bean <rbean@redhat.com> - 1.5.1-3
- Bump version to pick up gating.yaml file.

* Fri Nov 02 2018 Ralph Bean <rbean@redhat.com> - 1.5.1-2
- Bump version to pick up gating.yaml file.

* Fri Oct 19 2018 Ralph Bean <rbean@redhat.com> - 1.5.1-1
- New version
- Dropped python2 subpackage and modernized macros.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Ralph Bean <rbean@redhat.com> - 1.2.0-5
- Bump to try and trigger automated tests.

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Aug 09 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.0-3
- Python 2 binary package renamed to python2-ansi2html
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Ralph Bean <rbean@redhat.com> - 1.2.0-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar 02 2016 Ralph Bean <rbean@redhat.com> - 1.1.1-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 30 2015 Ralph Bean <rbean@redhat.com> - 1.1.0-1
- new version

* Wed Jan 28 2015 Ralph Bean <rbean@redhat.com> - 1.0.6-6
- Bump spec for testing.

* Mon Oct 13 2014 Ralph Bean <rbean@redhat.com> - 1.0.6-5
- Modernized python2 macros.
- Remove any bundled egg-info.
- BR on python2-devel.

* Wed Aug 27 2014 Ralph Bean <rbean@redhat.com> - 1.0.6-4
- Added explicit dependency on python(3)-setuptools.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Jan 28 2014 Ralph Bean <rbean@redhat.com> - 1.0.6-1
- Latest upstream.

* Sat Oct 12 2013 Ralph Bean <rbean@redhat.com> - 1.0.5-1
- Latest upstream with configurable color scheme.

* Sat Oct 12 2013 Ralph Bean <rbean@redhat.com> - 1.0.3-1
- Latest upstream with a tweak to setup.py

* Fri Oct 04 2013 Ralph Bean <rbean@redhat.com> - 1.0.2-1
- Latest upstream.
- Manpages now included.

* Thu Sep 26 2013 Ralph Bean <rbean@redhat.com> - 0.10.0-3
- Latest upstream with a superior internal state model thanks to Sebastian
  Pipping.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Ralph Bean <rbean@redhat.com> - 0.9.4-2
- Removed python3 rhel conditional.

* Mon Feb 25 2013 Ralph Bean <rbean@redhat.com> - 0.9.4-1
- Latest upstream fixes encoding issues.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 26 2012 Ralph Bean <rbean@redhat.com> - 0.9.2-1
- New upstream
- Fixes dict ordering issues.
- Solves some encoding issues.

* Mon Aug  6 2012 David Malcolm <dmalcolm@redhat.com> - 0.9.1-8
- fix dict ordering issues

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 0.9.1-7
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Ralph Bean <rbean@redhat.com> - 0.9.1-5
- Re-enabled tests.
* Mon Jul 09 2012 Ralph Bean <rbean@redhat.com> - 0.9.1-4
- Temporarily removed both sets of tests until python-mock problems are sorted
  out.
* Mon Jul 09 2012 Ralph Bean <rbean@redhat.com> - 0.9.1-3
- Temporarily removed python3 tests until python3-mock is available.
* Mon Jul 09 2012 Ralph Bean <rbean@redhat.com> - 0.9.1-2
- Added requirements python-mock and python-ordereddict.
* Mon Jul 09 2012 Ralph Bean <rbean@redhat.com> - 0.9.1-1
- Latest upstream version.
* Tue Jun 26 2012 Ralph Bean <rbean@redhat.com> - 0.9.0-4
- Only Require python3 for python3-ansi2html.
* Wed May 23 2012 Ralph Bean <rbean@redhat.com> - 0.9.0-3
- Fix executable python2/python3 confusion.
- More explicit ownership of dirs in python_sitelib.
- Removed mixed use of tabs and spaces.
* Wed May 09 2012 Ralph Bean <rbean@redhat.com> - 0.9.0-2
- python3 support.
* Wed May 09 2012 Ralph Bean <rbean@redhat.com> - 0.9.0-1
- Packaged latest upstream version.
- Removed unnecessary defattr and buildroot
- New dependency on python-six
* Fri Feb 3 2012 Ralph Bean <rbean@redhat.com> - 0.8.3-1
- Included tests in check section.
- More concise file ownership declarations.
- Resolved license ambiguity in upstream.
- Removed shebang from non-executable file.
* Mon Jan 30 2012 Ralph Bean <rbean@redhat.com> - 0.8.2-1
- Updated ansi2html version to latest 0.8.2.
- Added _bindir entry for the ansi2html console-script.
- Removed dependency on genshi.
- Removed references to now EOL fedora 12.
* Wed Sep 15 2010 Ralph Bean <ralph.bean@gmail.com> - 0.5.2-1
- Updated spec based on comments from Mark McKinstry
* Tue Sep 7 2010 Ralph Bean <ralph.bean@gmail.com> - 0.5.1-1
- Initial RPM packaging

