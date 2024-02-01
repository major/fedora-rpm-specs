Name:           python-sphinx-inline-tabs
# There are 2 different versions here:
# https://github.com/pradyunsg/sphinx-inline-tabs/issues/7
Version:        2022.01.02~b11
%global tag     2022.01.02.beta11
Release:        %autorelease
Summary:        Add inline tabbed content to your Sphinx documentation
# SPDX
License:        MIT
URL:            https://github.com/pradyunsg/sphinx-inline-tabs
Source0:        %{url}/archive/%{tag}/sphinx-inline-tabs-%{tag}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

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


%prep
%autosetup -p1 -n sphinx-inline-tabs-%{tag}


%generate_buildrequires
# There is a [test] extra, but there are no tests :/
# https://github.com/pradyunsg/sphinx-inline-tabs/issues/6
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files sphinx_inline_tabs


%files -n python3-sphinx-inline-tabs -f %{pyproject_files}
%doc README.md
%doc CODE_OF_CONDUCT.md
%license LICENSE


%changelog
%autochangelog
