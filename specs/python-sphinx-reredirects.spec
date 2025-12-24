%global giturl  https://github.com/documatt/sphinx-reredirects

Name:           python-sphinx-reredirects
Version:        1.1.0
Release:        %autorelease
Summary:        Handle redirects for moved pages in Sphinx documentation

License:        MIT
URL:            https://documatt.com/sphinx-reredirects/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/sphinx-reredirects-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(install): -l sphinx_reredirects

BuildRequires:  %{py3_dist pytest}

%global _description %{expand:Sphinx-reredirects is the extension for Sphinx documentation projects that
handles redirects for moved pages.  It generates HTML pages with meta refresh
redirects to the new page location to prevent 404 errors if you rename or move
your documents.}

%description
%_description

%package     -n python3-sphinx-reredirects
Summary:        Handle redirects for moved pages in Sphinx documentation
# See https://pagure.io/packaging-committee/issue/1312.
# A duplicate python3-sphinx_reredirects was created that conflicts with this one.
# We Obsolete the duplicate and add Provides for python3-sphinx_reredirects to
# make this one easier to find.
%py_provides    python3-sphinx_reredirects
# This can be removed when F42 reaches EOL
Obsoletes:      python3-sphinx_reredirects < 0.1.2-3

# This can be removed when F46 reaches EOL
Obsoletes:      python3-sphinx-reredirects-doc < 1.0.0
Provides:       python3-sphinx-reredirects-doc = %{version}-%{release}

%description -n python3-sphinx-reredirects
%_description

%check
# test_linkcheck attempts to access the network
%pytest -k 'not test_linkcheck'

%files -n python3-sphinx-reredirects -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
