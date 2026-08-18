%global pypi_name medimages4tests

%global forgeurl https://github.com/australian-imaging-service/medimages4tests
%global version 0.5.9
%global tag     v%{version}
%forgemeta

Name:           python-%{pypi_name}
Version:        %forgeversion
Release:        %autorelease
Summary:        Generates dummy medical image for image handling tests

# The entire source is Apache-2.0, except that versioneer.py and the
# _version.py it generates are CC0-1.0, not generally allowed for code in
# Fedora, but OK under the exception for existing uses in Fedora prior to
# 2022-08-01. While these are included in the source RPM, we re-generate
# _version.py using the system python-versioneer, which is a later version
# under Unlicense so the resulting _version.py is also Unlicense.
License:        Apache-2.0 AND Unlicense
URL:            %forgeurl
Source:         %forgesource


BuildArch:      noarch
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Generate dummy medical images, with junk image data but realistic
headers, to test imaging handling pipelines.}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%forgeautosetup -p1 -S git

# Versioneer wants a tag to set version
# Make sure this is last in %%prep to avoid dev release
git add --all
git commit --allow-empty -m '[Fedora] Changes for RPM package'
git tag %{git_tag}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
# Exclude test requiring network
k="${k-}${k+ and }not test_openneuro_retrieve"
%pytest -r fEs ${k+-k }"${k-}"


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst AUTHORS


%changelog
%autochangelog
