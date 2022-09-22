Name:          python-tcolorpy
Version:       0.1.1
Release:       3%{?dist}
Summary:       Python library to apply true color for terminal text

License:       MIT
URL:           https://github.com/thombashi/tcolorpy
Source0:       %{pypi_source tcolorpy}

# Remove shebang from __main__.py. It makes no sense there
# Reported upstream https://github.com/thombashi/tcolorpy/issues/2
Patch0:        https://patch-diff.githubusercontent.com/raw/thombashi/tcolorpy/pull/3.patch

BuildArch:     noarch
BuildRequires: python3-devel

# tox.ini uses the [test] extra, see also https://github.com/thombashi/tcolorpy/pull/1
# the [test] extra brings in just pytest and pytest-md-report and we don't need the latter
# hence, manually specifying pytest instead:
BuildRequires: python3-pytest

%description
%{summary}.

%package -n python3-tcolorpy
Summary:        %{summary}

%description -n python3-tcolorpy
%{summary}.


%prep
%autosetup -p1 -n tcolorpy-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files tcolorpy


%check
%pytest


%files -n python3-tcolorpy -f %{pyproject_files}
%doc README.rst


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.1-2
- Rebuilt for Python 3.11

* Fri Feb 25 2022 Jonny Heggheim <hegjon@gmail.com> - 0.1.1-1
- Initial package
