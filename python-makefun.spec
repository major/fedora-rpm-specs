Name:		python-makefun
Version:	1.15.2
Release:	%autorelease
Summary:	Dynamically create python functions with a proper signature

License:	BSD
URL:		https://pypi.org/project/makefun
Source0:	%{pypi_source makefun}

BuildArch:	noarch
BuildRequires:	pyproject-rpm-macros

%global _description \
%summary.

%description %_description

%package -n python3-makefun
Summary: %{summary}
%{?python_provide:%python_provide python3-makefun}

%description -n python3-makefun %_description

%prep
%autosetup -n makefun-%{version}

cat >pyproject.toml <<EOF
[build-system]
requires = ["pytest-runner", "setuptools_scm", "pypandoc", "six", "wheel"]
build-backend = "setuptools.build_meta"
EOF

sed -r -i "s/'pandoc', //" setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
# Tests require pytest-cases, which requires this package. Yay!
PYTHONPATH=%{buildroot}/%{python3_sitelib} \
    %python3 -m pytest -v

%files -n python3-makefun
%license LICENSE
%doc README.md
%{python3_sitelib}/makefun/
%{python3_sitelib}/makefun-%{version}.dist-info/

%changelog
%autochangelog
