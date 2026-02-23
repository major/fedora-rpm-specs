%global srcname sphinx-favicon
%global modname sphinx_favicon

Name:           python-%{srcname}
Version:        1.1.0
Release:        %autorelease
Summary:        Sphinx extension to add custom favicons

License:        MIT
URL:            https://github.com/tcmetzger/sphinx-favicon
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
A Sphinx extension to add custom favicons

With Sphinx Favicon, you can add custom favicons to your Sphinx html
documentation quickly and easily.

You can define favicons directly in your conf.py, with different rel
attributes such as "icon" or "apple-touch-icon" and any favicon size.

The Sphinx Favicon extension gives you more flexibility than the standard
favicon.ico supported by Sphinx. It provides a quick and easy way to add the
most important favicon formats for different browsers and devices.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}
sed -i -e 's/, "pytest-cov"//' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{modname}

%check
# tests/test_options.py::test_list_of_three_icons_automated_values requires network access
%pytest -v --deselect tests/test_options.py::test_list_of_three_icons_automated_values

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG

%changelog
%autochangelog
