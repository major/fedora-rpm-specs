%global pypi_name openstackdocstheme

Name:           python-%{pypi_name}
Version:        3.5.0
Release:        %autorelease
Summary:        OpenStack Docs Theme

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://docs.openstack.org/
Source0:        %{pypi_source}
Patch0001:      0001-Remove-all-Google-Analytics-tracking.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-sphinx
BuildRequires:  git-core

%global common_desc \
OpenStack docs.openstack.org Sphinx Theme\
\
Theme and extension support for Sphinx documentation that is published to\
docs.openstack.org. Intended for use by OpenStack projects.

%description
%{common_desc}


%package -n     python3-%{pypi_name}
Summary:        OpenStack Docs Theme
%{?python_provide:%python_provide python3-%{pypi_name}}
Provides:       bundled(js-jquery)

Requires: python3-sphinx >= 1.6.2
Requires: python3-babel

%description -n python3-%{pypi_name}
%{common_desc}

%package -n     python-%{pypi_name}-doc
Summary:        openstackdocstheme documentation
%description -n python-%{pypi_name}-doc
Documentation for openstackdocstheme


%generate_buildrequires
%pyproject_buildrequires


%prep
%autosetup -n %{pypi_name}-%{version} -p1 -S git
# Make sure there is no Google Analytics
sed -i 's/analytics_tracking_code.*/analytics_tracking_code\ =/' openstackdocstheme/theme/openstackdocs/theme.conf
# Prevent doc build warnings from causing a build failure
sed -i '/warning-is-error/d' setup.cfg

%build
%pyproject_wheel

export PYTHONPATH=.
sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/docstheme-build-pdf
%{_bindir}/docstheme-build-translated.sh
%{_bindir}/docstheme-lang-display-name.py

%files -n python-%{pypi_name}-doc
%doc doc/build/html

%changelog
%autochangelog
