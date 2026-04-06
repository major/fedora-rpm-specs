%global pypi_name sphinxcontrib-pecanwsme

%global _description %{expand:
This is an extension to Sphinx (http://sphinx-doc.org/) for documenting APIs
built with the Pecan WSGI object-dispatching web framework and WSME
(Web Services Made Easy).}


Name:           python-%{pypi_name}
Version:        0.11.0
Release:        %autorelease
Summary:        Extension to Sphinx for documenting APIs built with Pecan and WSME

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/dreamhost/sphinxcontrib-pecanwsme
Source0:        https://pypi.python.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel


%description %_description


%package -n python3-%{pypi_name}
Summary:        Extension to Sphinx for documenting APIs built with Pecan and WSME


%description -n python3-%{pypi_name} %_description


%prep
%autosetup -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l sphinxcontrib


%check
%pyproject_check_import sphinxcontrib.pecanwsme -e sphinxcontrib.pecanwsme.rest


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{python3_sitelib}/sphinxcontrib_pecanwsme-*.pth


%changelog
%autochangelog
