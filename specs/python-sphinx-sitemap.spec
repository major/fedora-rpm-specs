%global giturl  https://github.com/jdillard/sphinx-sitemap

Name:           python-sphinx-sitemap
Version:        2.6.0
Release:        %autorelease
Summary:        Sitemap generator for Sphinx

License:        MIT
URL:            https://sphinx-sitemap.readthedocs.io/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/sphinx-sitemap-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This package contains a Sphinx extension to generate multiversion and
multilanguage sitemaps.org-compliant sitemaps for the HTML version of
your Sphinx documentation.}

%description %_description

%package     -n python3-sphinx-sitemap
Summary:        Sitemap generator for Sphinx

%description -n python3-sphinx-sitemap %_description

%prep
%autosetup -n sphinx-sitemap-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel
rst2html --no-datestamp README.rst README.html

%install
%pyproject_install
%pyproject_save_files -l sphinx_sitemap

%check
%tox

%files -n python3-sphinx-sitemap -f %{pyproject_files}
%doc README.html

%changelog
%autochangelog
