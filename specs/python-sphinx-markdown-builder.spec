Summary:        Sphinx extension for rendering markdown builder
Name:           python-sphinx-markdown-builder
Version:        0.6.8
Release:        %autorelease
License:        MIT
URL:            https://github.com/liran-funaro/sphinx-markdown-builder
Source0:        https://github.com/liran-funaro/sphinx-markdown-builder/archive/%{version}/sphinx-markdown-builder-%{version}.tar.gz
# https://github.com/liran-funaro/sphinx-markdown-builder/commit/967edca
Patch:          0001-Update-test-config.patch
# https://github.com/liran-funaro/sphinx-markdown-builder/pull/39
Patch:          0002-Convert-to-updated-SPDX-license-expression.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3-sphinxcontrib-httpdomain
%description
A Sphinx extension for rendering builder written in markdown.

%package     -n python3-sphinx-markdown-builder
Summary:        Sphinx extension for rendering markdown builder

%description -n python3-sphinx-markdown-builder
A Sphinx extension for rendering builder written in markdown.

%prep
%autosetup -p1 -n sphinx-markdown-builder-%{version}
%if 0%{fedora} < 43
sed -i -e 's/license = "MIT"/license = { text = "MIT" }/' pyproject.toml
%endif
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l sphinx_markdown_builder

%check
%pyproject_check_import
%pytest

%files -n python3-sphinx-markdown-builder -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
