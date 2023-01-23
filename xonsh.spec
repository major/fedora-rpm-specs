Name:           xonsh
Version:        0.13.3
Release:        2%{?dist}
Summary:        A general purpose, Python-ish shell

# xonsh is BSD-2-Clause.
# xonsh/winutils.py and xonsh/xoreutils/_which.py contain MIT code.
License:        BSD and MIT
URL:            https://xon.sh
Source0:        %pypi_source
BuildArch:      noarch

Patch1: 0001-Do-not-use-custom-xinstall.patch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist wheel}
BuildRequires:  %{py3_dist prompt-toolkit}
BuildRequires:  %{py3_dist pyperclip}
BuildRequires:  %{py3_dist setproctitle}
BuildRequires:  %{py3_dist pygments}
BuildRequires:  %{py3_dist distro}
BuildRequires:  %{py3_dist ujson}
BuildRequires:  %{py3_dist virtualenv}
BuildRequires:  %{py3_dist ply}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-mock}
BuildRequires:  %{py3_dist pytest-subprocess}
BuildRequires:  %{py3_dist pytest-rerunfailures}
BuildRequires:  %{py3_dist pyte}
BuildRequires:  bash-completion
BuildRequires:  git-core
BuildRequires:  man-db
# needed for tests:
BuildRequires:  /usr/bin/python
BuildRequires:  /usr/bin/pip3

# required by "ptk" extra:
Requires:       %{py3_dist prompt-toolkit}
Requires:       %{py3_dist pygments}
Requires:       %{py3_dist pyperclip}

# required by "setproctitle" extra:
Requires:       %{py3_dist setproctitle}

# required by "full" extra:
Requires:       %{py3_dist distro}
Requires:       %{py3_dist ujson}

# unbundled in prep
Requires:       %{py3_dist ply}

# required for vox
Requires:       %{py3_dist virtualenv}

Recommends:     bash-completion

%description
xonsh is a Python-powered, cross-platform, Unix-gazing shell language and
command prompt.

The language is a superset of Python 3.6+ with additional shell primitives.
xonsh (pronounced conch) is meant for the daily use of experts and novices
alike.

%prep
%autosetup -n %{name}-%{version}

# Unbundle ply
sed --in-place '/xonsh\.ply/d' setup.py
sed --in-place '/xonsh\.ply/d' pyproject.toml
sed --in-place -e 's/xonsh\.ply\.ply/ply/' \
               -e 's/from xonsh\.ply //' \
               $(grep -rl --include='*.py' 'xonsh\.ply')
rm -r xonsh/ply

# Remove shebang.
sed --in-place "s:#!\s*/usr.*::" xonsh/xoreutils/_which.py xonsh/webconfig/main.py

%build
%py3_build

%install
%py3_install

%check
# Altering PYTHONPATH makes the tests importable.
%global __pytest PYTHONPATH="$PYTHONPATH:$(pwd)" %{python3} -m xonsh run-tests.xsh test --
# TODO: broken tests
%pytest -k "not test_complete_dots and not test_vox"

%post
if [ "$1" -ge 1 ]; then
  if [ ! -f %{_sysconfdir}/shells ] ; then
    touch %{_sysconfdir}/shells
  fi
  for binpath in %{_bindir} /bin; do
    if ! grep -q "^${binpath}/xonsh$" %{_sysconfdir}/shells; then
       (cat %{_sysconfdir}/shells; echo "$binpath/xonsh") > %{_sysconfdir}/shells.new
       mv %{_sysconfdir}/shells{.new,}
    fi
  done
fi

%postun
if [ "$1" = 0 ] && [ -f %{_sysconfdir}/shells ] ; then
  sed -e '\!^%{_bindir}/xonsh$!d' -e '\!^/bin/xonsh$!d' < %{_sysconfdir}/shells > %{_sysconfdir}/shells.new
  mv %{_sysconfdir}/shells{.new,}
fi

%files
%doc README.rst
%license license
%{_bindir}/xonsh
%{_bindir}/xonsh-cat
%{_bindir}/xonsh-uname
%{_bindir}/xonsh-uptime
%{python3_sitelib}/xompletions/
%{python3_sitelib}/xonsh/
%{python3_sitelib}/xontrib/
%{python3_sitelib}/xonsh-%{version}*-py%{python3_version}.egg-info/

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Oct 06 2022 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.13.3-1
- new version

* Fri Aug 26 2022 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.13.1-1
- new version

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.11.0-4
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 16 2021 Carmen Bianca Bakker <carmenbiance@fedoraproject.org> - 0.11.0-2
- Recommend bash-completion.
- Depend on pyperclip.
- Run more tests during build process.

* Tue Nov 23 2021 Carmen Bianca Bakker <carmen@carmenbianca.eu> - 0.11.0-1
- new version

* Mon Jul 26 2021 Miro Hrončok <mhroncok@redhat.com> - 0.10.1-1
- Update to 0.10.1
- Fixes rhbz#1899842
- Fixes rhbz#1934672

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.26-2
- Rebuilt for Python 3.10

* Thu Feb 04 2021 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.9.26-1
- Update to 0.9.26

* Fri Jan 29 2021 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.9.25-1
- Update to 0.9.25

* Tue Jan 26 14:29:37 CEST 2021 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.9.24-1
- new version

* Thu Sep 10 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.21-1
- Rebuilt for Python 3.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild
- Update to 0.9.21
- Unbundle ply
- Fixes: rhbz#1817770
- Fixes: rhbz#1822355

* Fri Apr 10 2020 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.9.17-1
- new version

* Tue Apr 07 2020 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.9.16-1
- new version

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 22 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.9.13-1
- New upstream version.
- Python 3.8 should no longer crash.

* Thu Sep 05 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.9.11-3
- Re-enable tests.

* Tue Sep 03 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.9.11-2
- Temporarily disable tests for Python 3.8

* Thu Aug 29 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.9.11-1
- new version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.10-3
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.10-2
- Rebuilt for Python 3.8

* Tue Aug 13 2019 Mairi Dulaney <jdulaney@fedoraproject.org> - 0.9.10-1
- Upgrade to latest release

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.9.6-1
- new version

* Sat May 18 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.9.3-1
- New upstream version

* Fri May 10 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.9.0-1
- New upstream version
- Python 3.4 support deprecated
- Tentative Python 3.8 support added

* Tue Apr 23 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.8.12-2
- Automatically add/remove xonsh to /etc/shells.

* Tue Apr 02 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.8.12-1
- New upstream release 0.8.12

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 John Dulaney <jdulaney@fedoraproject.org> - 0.6.9-1
- New upstream release

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.5-2
- Rebuilt for Python 3.7

* Thu May 31 2018 John Dulaney <jdulaney@fedoraproject.org> - 0.6.5-1
- New upstream release

* Sat Apr 14 2018 John Dulaney <jdulaney@fedoraproject.org> - 0.6.1-1
- New upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 John Dulaney <jdulaney@fedoraproject.org> - 0.5.12-1
- New upstream release 0.5.12

* Mon May 29 2017 John Dulaney <jdulaney@fedoraproject.org> - 0.5.10-1
- New upstream release 0.5.10

* Tue Apr 04 2017 John Dulaney <jdulaney@fedoraproject.org> - 0.5.9-1
- New upstream release 0.5.9

* Sat Mar 11 2017 John Dulaney <jdulaney@fedoraproject.org> - 0.5.8-1
- New upstream release 0.5.8

* Fri Mar 03 2017 John Dulaney <jdulaney@fedoraproject.org> - 0.5.7-1
- New upstream release 0.5.7

* Fri Feb 24 2017 John Dulaney <jdulaney@fedoraproject.org> - 0.5.6-1
- New upstream release 0.5.6

* Sun Feb 12 2017 John Dulaney <jdulaney@fedoraproject.org> - 0.5.4-1
- New upstream release 0.5.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 07 2017 John Dulaney <jdulaney@fedoraproject.org> - 0.5.2-1
- New upstream release 0.5.2

* Sat Dec 24 2016 John Dulaney <jdulaney@fedoraproject.org> - 0.5.1
- New upstream release 0.5.1

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.7-2
- Rebuild for Python 3.6

* Mon Oct 03 2016 John Dulaney <jdulaney@fedoraproject.org> - 0.4.7-1
- New upstream release 0.4.7

* Sun Sep 04 2016 John Dulaney <jdulaney@fedoraproject.org> - 0.4.6-1
- New upstream release 0.4.6

* Sun Aug 28 2016 John Dulaney <jdulaney@fedoraproject.org> - 0.4.5-2
- Require python3-pygments and python3-setproctitle

* Sun Aug 28 2016 John Dulaney <jdulaney@fedoraproject.org> - 0.4.5-1
- New upstream release 0.4.5

* Fri Aug  5 2016 Luke Macken <lmacken@redhat.com> - 0.4.4-2
- Require python3-prompt_toolkit to improve usability

* Thu Jul 21 2016 John Dulaney <jdulaney@fedoraproject.org> - 0.4.4-1
- New upstream release 0.4.4

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 13 2016 John Dulaney <jdulaney@fedoraproject.org> - 0.4.3-1
- New upstream release 0.4.3

* Mon Jun 20 2016 Luke Macken <lmacken@redhat.com> - 0.3.4-1
- New upstream release 0.3.4

* Mon Jun 06 2016 Luke Macken <lmacken@redhat.com> - 0.3.3-1
- Latest upstream release
- Update the URL

* Fri Jun 03 2016 Luke Macken <lmacken@redhat.com> - 0.3.2-1
- Latest upstream release
- Update the Summary

* Mon Mar 16 2015 Robert Kuska <rkuska@redhat.com> - 0.1.2-1
- Initial package.
