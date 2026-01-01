Name:           python-sphinx-inline-tabs
Version:        2025.12.21.14
Release:        %autorelease
Summary:        Add inline tabbed content to your Sphinx documentation
# SPDX
License:        MIT
URL:            https://github.com/pradyunsg/sphinx-inline-tabs
Source:         %{url}/archive/%{version}/sphinx-inline-tabs-%{version}.tar.gz

# Make tests runnable in %%check, merged upstream
Patch:          https://github.com/pradyunsg/sphinx-inline-tabs/pull/53.patch

BuildArch:      noarch

BuildSystem:    pyproject
BuildOption(generate_buildrequires): -x test
BuildOption(install): -l sphinx_inline_tabs


%global _description %{expand:
Add inline tabbed content to your Sphinx documentation.

Features:

- Elegant design: Small footprint in the markup and generated website,
  while looking good.
- Configurable: All the colors can be configured using CSS variables.
- Synchronization: Tabs with the same label all switch with a single click.
- Works without JavaScript: JavaScript is not required for the basics, only for
  synchronization.}

%description %_description


%package -n python3-sphinx-inline-tabs
Summary:        %{summary}

%description -n python3-sphinx-inline-tabs  %_description


%prep -a
sed -i '/pytest-cov/d' pyproject.toml


%check -a
# As of 2025.12.21.14, the deselected tests assert docutils 0.21.2 specifcic output.
%pytest -k "not xml"


%files -n python3-sphinx-inline-tabs -f %{pyproject_files}
%doc README.md
%doc CODE_OF_CONDUCT.md


%changelog
%autochangelog
