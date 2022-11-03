Name:           python-nb2plots
Version:        0.6.1
Release:        4%{?dist}
Summary:        Convert between Jupyter notebooks and sphinx docs

License:        BSD-2-Clause
URL:            https://matthew-brett.github.io/nb2plots/
Source0:        https://github.com/matthew-brett/nb2plots/archive/%{version}/nb2plots-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist ipykernel}
BuildRequires:  %{py3_dist ipython}
BuildRequires:  %{py3_dist jupyter-client}
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist nbconvert}
BuildRequires:  %{py3_dist netifaces}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist numpydoc}
BuildRequires:  %{py3_dist pip}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist scripttester}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist six}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinxtesters}
BuildRequires:  %{py3_dist texext}
BuildRequires:  %{py3_dist wheel}

BuildRequires:  help2man
BuildRequires:  latexmk
BuildRequires:  make
BuildRequires:  pandoc
BuildRequires:  tex(latex)
BuildRequires:  tex(capt-of.sty)
BuildRequires:  tex(fncychap.sty)
BuildRequires:  tex(framed.sty)
BuildRequires:  tex(needspace.sty)
BuildRequires:  tex(tabulary.sty)
BuildRequires:  tex(upquote.sty)
BuildRequires:  tex(wrapfig.sty)

%description
This package contains tools for converting from Jupyter notebooks to
ReST for Sphinx, and vice versa.

%package -n     python3-nb2plots
Summary:        Convert between Jupyter notebooks and sphinx docs
Requires:       pandoc
Requires:       %{py3_dist ipykernel}
Requires:       %{py3_dist jupyter-client}
Requires:       %{py3_dist nbconvert}

%description -n python3-nb2plots
This package contains tools for converting from Jupyter notebooks to
ReST for Sphinx, and vice versa.

%package docs
Summary:        Documentation for %{name}

%description docs
Documentation for %{name}.

%prep
%autosetup -p1 -n nb2plots-%{version}
# The ghp-import requirement is needed only for pushing to github
sed -i '/ghp-import/d' doc-requirements.txt

# The mock import is only needed for python < 3.3
sed -i '/mock/d' test-requirements.txt

# Fix shebangs
%py3_shebang_fix scripts/* setup.py doc/conf.py
sed -i '/#!python/d' nb2plots/from_notebook.py

%build
%pyproject_wheel
%py3_shebang_fix build/scripts-*/*

# Documentation build
export PATH=$PWD/build/scripts-%{python3_version}:$PATH
export PYTHONPATH=%{pyproject_build_lib}
make -C doc html
rst2html --no-datestamp README.rst README.html

# Make man pages
mkdir man1
for m in nb2plots rst2md sphinx2md sphinx2nb sphinx2pxml sphinx2py; do
  help2man --version-string=%{version} -N -o man1/${m}.1 scripts/$m
done

%install
%pyproject_install
%pyproject_save_files nb2plots

# Install the man pages
mkdir -p %{buildroot}%{_mandir}
cp -a man1 %{buildroot}%{_mandir}

%check
%pytest

%files -n python3-nb2plots -f %{pyproject_files}
%doc Changelog README.html
%{_bindir}/nb2plots
%{_bindir}/rst2md
%{_bindir}/sphinx2md
%{_bindir}/sphinx2nb
%{_bindir}/sphinx2pxml
%{_bindir}/sphinx2py
%{_mandir}/man1/*

%files docs
%doc doc/_build/html/*

%changelog
* Tue Nov  1 2022 Jerry James <loganjerry@gmail.com> - 0.6.1-4
- Use %%py3_shebang_fix instead of invoking pathfix.py directly
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 0.6.1-2
- Rebuilt for Python 3.11

* Fri Jun  3 2022 Jerry James <loganjerry@gmail.com> - 0.6.1-1
- Version 0.6.1
- All patches have been upstreamed

* Mon Feb 28 2022 Lumír Balhar <lbalhar@redhat.com> - 0.6-20.20201224.1a7bac4
- Fix tests for newer dependencies

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-19.20201224.1a7bac4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 Jerry James <loganjerry@gmail.com> - 0.6-18.20201224.1a7bac4
- Add -versioneer patch to fix FTBFS with python 3.11

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-17.20201224.1a7bac4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6-16.20201224.1a7bac4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-15.20201224.1a7bac4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Jerry James <loganjerry@gmail.com> - 0.6-14.20201224.1a7bac4
- Update to git head for nbconvert 6.x fixes
- Remove unused dependency on python3-mock package

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-13.20200412.bdcaeb7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6-12.20200412.bdcaeb7
- Rebuilt for Python 3.9

* Sun Apr 19 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6-11.20200412.bdcaeb7
- Ensure the Python package version matches the RPM package version

* Sat Apr 18 2020 Jerry James <loganjerry@gmail.com> - 0.6-10.20200412.bdcaeb7
- Update to git head for sphinx 3 fixes
- Drop upstreamed -escape and -abc patches

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-9.20190809.dfa3ad2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Jerry James <loganjerry@gmail.com> - 0.6-8.20190809.dfa3ad2
- Add -escape and -abc patches to silence python 3.8 warnings
- Add man pages

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6-7.20190809.dfa3ad2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6-6.20190809.dfa3ad2
- Rebuilt for Python 3.8

* Tue Aug 13 2019 Jerry James <loganjerry@gmail.com> - 0.6-5.20190809.dfa3ad2
- Update to 20190809 git snapshot for Sphinx 2 fixes
- Drop -sphinxtesters patch

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 07 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6-3
- Drop the python2 subpackage

* Sat Sep  8 2018 Jerry James <loganjerry@gmail.com> - 0.6-2
- Fix problems found on review

* Wed Sep  5 2018 Jerry James <loganjerry@gmail.com> - 0.6-1
- Initial RPM
