%global         srcname         sphinx-argparse-cli
%global         importname      sphinx_argparse_cli
%global         forgeurl        https://github.com/tox-dev/sphinx-argparse-cli
Version:        1.21.3
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Render CLI arguments defined by the argparse module

License:        MIT
URL:            %forgeurl
Source:         %{url}/archive/%{version}/sphinx-argparse-cli-%{version}.tar.gz
Patch:          no-coverage.patch

BuildRequires:  python3-devel
BuildArch: noarch

%global _description %{expand:
Render CLI arguments (sub-commands friendly) defined by the argparse module.
For live demo check out the documentation of tox, pypa-build and mdpo.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}
sed -i '/name = "sphinx-argparse-cli"/a version = "%{version}"' \
  pyproject.toml
sed -i '/version.source = "vcs"/d' pyproject.toml
sed -i '/"version",/{n;d;}' pyproject.toml
sed -i '/  "version",/d' pyproject.toml
sed -i '/^dynamic = \[/d' pyproject.toml
# relax version requirement
sed -i 's/sphinx>=9.0.4/sphinx>=8.2.3/g' pyproject.toml
ver=%{version}
ver_comma=${ver//./, }
touch version.py
echo "__version__ = version = '%{version}'" > version.py
echo "__version_tuple__ = version_tuple = (${ver_comma})" >> version.py
mv version.py src/sphinx_argparse_cli/
chmod 644 src/sphinx_argparse_cli/version.py

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{importname}

%check
%pyproject_check_import
%tox -- -- --verbose

%files -n python3-%{srcname} -f %{pyproject_files}
 
%changelog
%autochangelog
