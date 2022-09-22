%bcond_without tests

%global _description %{expand:
PyPhi is a Python library for computing integrated information, and the
associated quantities and objects.

If you use this code, please cite the manuscript:

Mayner WGP, Marshall W, Albantakis L, Findlay G, Marchman R, Tononi G (2017).
PyPhi: A toolbox for integrated information. arXiv:1712.09644 [q-bio.NC].

The manuscript is available at https://arxiv.org/abs/1712.09644.}

%global forgeurl  https://github.com/wmayner/pyphi/

Name:           python-pyphi
Version:        1.2.1
Release:        %autorelease
Summary:        A library for computing integrated information

%global tag  %{version}
%forgemeta

License:        GPLv3
URL:            %forgeurl
Source0:        %forgesource
# https://github.com/wmayner/pyphi/pull/50
Patch0:         0001-fix-py3.10-correct-collections-import.patch
BuildRequires:  git-core
BuildArch:      noarch

# Tests fails on s390x: https://github.com/wmayner/pyphi/issues/41
ExcludeArch:    s390x

%description %_description

%package -n python3-pyphi
Summary:        %{summary}
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-lazy-fixture}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}

%description -n python3-pyphi %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}


%prep
%autosetup -n pyphi-%{version} -S git

# sphinx 1.3+, it's an extension
# Also sent upstream: https://github.com/wmayner/pyphi/pull/22
sed -i "s/sphinxcontrib.napoleon/sphinx.ext.napoleon/" docs/conf.py

find pyphi -name "*.py" -exec sed -i '/#!\/usr\/bin\/env python3/ d' '{}' \;

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

make -C docs SPHINXBUILD=sphinx-build-3 html
rm docs/_build/html/{.doctrees,.buildinfo} -vf

%install
%pyproject_install
%pyproject_save_files pyphi

%check
%if %{with tests}
%{pytest}
%endif

%files -n python3-pyphi -f %{pyproject_files}
%doc README.md CHANGELOG.md CACHING.rst redis.conf

%files doc
%license LICENSE.md
%doc docs/_build/html/

%changelog
%autochangelog

* Wed Aug 18 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.2.0-13
- Correctly disable tests on s390x

* Wed Aug 18 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.2.0-12
- Fix build

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.0-10
- Rebuilt for Python 3.10

* Fri Jan 29 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.2.0-9
- Update URL

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.2.0-2
- Enable tests

* Sat Jun 22 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.2.0-1
- Update to 1.2.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.1.0-2
- Update license
- Fix doc generation
- Correct rpmlint errors

* Wed Nov 14 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.1.0-1
- Initial rpm build
