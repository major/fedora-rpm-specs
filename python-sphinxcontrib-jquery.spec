Name:           python-sphinxcontrib-jquery
Version:        3.0.0
Release:        1%{?dist}
Summary:        Extension to include jQuery on newer Sphinx releases

# The project is 0BSD
# _sphinx_javascript_frameworks_compat.js is BSD-2-Clause
# jquery-3.6.0.js and jquery.js are MIT
License:        0BSD AND BSD-2-Clause AND MIT
URL:            https://github.com/sphinx-contrib/jquery/
Source:         %{url}/archive/v%{version}/sphinxcontrib-jquery-%{version}.tar.gz

# This is a leftover dependency that isn't needed in the package anymore
# (it uses flit to build)
# Patch submitted upstream: https://github.com/sphinx-contrib/jquery/pull/22
Patch:          https://github.com/sphinx-contrib/jquery/pull/22.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# Test dependencies
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx

%global _description %{expand:
sphinxcontrib-jquery is a Sphinx extension that ensures that jQuery
is always installed for use in Sphinx themes or extensions.}


%description %_description

%package -n     python3-sphinxcontrib-jquery
Summary:        %{summary}
# The other sphinxcontrib packages require Sphinx in their metadata
# This one doesn't, so the upstream was queried about it:
# https://github.com/sphinx-contrib/jquery/issues/19
# Until then, it makes sense to explicitly require Sphinx in Fedora
Requires:       python3-sphinx

%description -n python3-sphinxcontrib-jquery %_description


%prep
%autosetup -p1 -n jquery-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files 'sphinxcontrib*'


%check
%pytest


%files -n python3-sphinxcontrib-jquery -f %{pyproject_files}
%doc README.rst
%license LICENCE


%changelog
* Mon Feb 27 2023 Karolina Surma <ksurma@redhat.com> - 3.0.0-1
- Initial package
