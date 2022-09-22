Name:           python-jupyter-sphinx
Version:        0.4.0
Release:        2%{?dist}
Summary:        Jupyter Sphinx extensions
License:        BSD
URL:            https://jupyter-sphinx.readthedocs.io/
Source0:        https://github.com/jupyter/jupyter-sphinx/archive/v%{version}/jupyter-sphinx-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist bash-kernel}
BuildRequires:  %{py3_dist ipython}
BuildRequires:  %{py3_dist ipywidgets}
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist nbconvert}
BuildRequires:  %{py3_dist nbformat}
BuildRequires:  %{py3_dist pip}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist wheel}

%global _desc %{expand:
Jupyter-Sphinx enables running code embedded in Sphinx documentation and
embedding output of that code into the resulting document.  It has
support for rich output such as images and even Jupyter interactive
widgets.}

%description %_desc

%package -n python3-jupyter-sphinx
Summary:        %{summary}

%description -n python3-jupyter-sphinx %_desc

%package        doc
Summary:        Documentation for %{name}

%description    doc
Documentation for %{name}.

%prep
%autosetup -n jupyter-sphinx-%{version} -p1

%build
%pyproject_wheel

# Build the documentation
PYTHONPATH=$PWD make -C doc html
rm doc/build/html/.buildinfo

%install
%pyproject_install
%pyproject_save_files jupyter_sphinx

%check
%pytest

%files -n python3-jupyter-sphinx -f %{pyproject_files}
%doc README.md

%files doc
%doc doc/build/html

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 25 2022 Jerry James <loganjerry@gmail.com> - 0.4.0-1
- Version 0.4.0
- Drop upstreamed -bash patch

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.3.2-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Jerry James <loganjerry@gmail.com> - 0.3.2-1
- Initial RPM
