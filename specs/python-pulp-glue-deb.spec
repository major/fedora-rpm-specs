Name: python-pulp-glue-deb
Version: 0.4.3
Release: %autorelease
Summary: The version agnostic Pulp 3 client library in python (deb plugin)
License: GPL-2.0-or-later
URL: https://github.com/pulp/pulp-cli-deb
BuildArch: noarch

Source: %{url}/archive/%{version}/pulp-cli-deb-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3-pytest

%global _description %{expand:
pulp-glue is a library to ease the programmatic communication with the Pulp3
API. It helps to abstract different resource types with so called contexts and
allows to build or even provides complex workflows like chunked upload or
waiting on tasks.
It is built around an openapi3 parser to provide client side validation of http
requests, while accounting for known quirks and incompatibilities between
different Pulp server component versions.}

%description %_description

%package -n python3-pulp-glue-deb
Summary: %{summary}

%description -n python3-pulp-glue-deb %_description

%prep
%autosetup -p1 -n pulp-cli-deb-%{version}/pulp-glue-deb

# Remove the Python version upper bound to enable building with new versions in Fedora
# This will work up until 3.19, which should be enough for now
sed -i '/requires-python =/s/,<3\.[0-9]\+//' pyproject.toml

# Remove upper version bound on setuptools to enable building with new versions in Fedora
sed -i '/requires =.*setuptools/s/<[0-9]\+//' pyproject.toml

# Remove upper version bound on packaging to enable building with new versions in Fedora
sed -i 's/"packaging.*"/"packaging"/' pyproject.toml

# Remove upper version bound on multidict to enable building with new versions in Fedora
sed -i '/"multidict/s/,<[0-9.]\+//' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pulp_glue

%files -n python3-pulp-glue-deb -f %{pyproject_files}
%license ../LICENSE
%doc README.*

%changelog
%autochangelog
