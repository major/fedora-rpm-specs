Name:           python-sphinxext-rediraffe
Version:        0.2.7
Release:        3%{?dist}
Summary:        Sphinx extension to redirect nonexistent pages
License:        MIT
URL:            https://wpilib.org/
Source0:        https://github.com/wpilibsuite/sphinxext-rediraffe/archive/v%{version}/sphinxext-rediraffe-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist jinja2}
BuildRequires:  %{py3_dist pip}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist wheel}

%global _desc %{expand:
This sphinx extension redirects non-existent pages to working pages.
Rediraffe can also check that deleted/renamed files in your git repo are
redirected.

Rediraffe creates a graph of all specified redirects and traverses it to
point all internal urls to leaf urls.  This means that chained redirects
will be resolved.  For example, if a config has 6 chained redirects, all
6 links will redirect directly to the final link.  The end user will
never experience more than 1 redirection.

Note: Rediraffe supports the html and dirhtml builders.}

%description %_desc

%package     -n python3-sphinxext-rediraffe
Summary:        %{summary}

%description -n python3-sphinxext-rediraffe %_desc

%prep
%autosetup -n sphinxext-rediraffe-%{version}

# The package needs jinja2 to function, but setup.py doesn't say so
sed -i '/install_requires/s/\[/&"jinja2", /' setup.py

# Retrieving the version with git fails
sed -i 's/main/%{version}/' setup.py

%build
%pyproject_wheel

%check
# The tests fail due to a missing dependency on seleniumbase
%pyproject_check_import

%install
%pyproject_install
%pyproject_save_files 'sphinxext*'

%files -n python3-sphinxext-rediraffe -f %{pyproject_files}
%doc README.md

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.7-2
- Rebuilt for Python 3.11

* Fri Apr 29 2022 Jerry James <loganjerry@gmail.com> - 0.2.7-1
- Initial RPM
