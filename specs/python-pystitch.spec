Name:           python-pystitch
Version:        1.0.0
Release:        %autorelease
Summary:        Embroidery IO library

License:        MIT
URL:            https://github.com/inkstitch/pystitch
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/pystitch-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
Python library for the reading and writing of embroidery files.

pystitch was coded from the ground up with all projects in mind. It includes a
lot of high and middle level pattern composition abilities, and should account
for any known error. If you know an error it does not account for, raise an
issue. It should be highly robust with a simple api so as to be reasonable for
any python embroidery project.

It should be complex enough to go very easily from points to stitches, fine
grained enough to let you control everything, and good enough that you shouldn't
want to.}

%description %_description

%package -n     python3-pystitch
Summary:        %{summary}

%description -n python3-pystitch %_description


%prep
%autosetup -p1 -n pystitch-%{version}
# Use older license declarations for f42 and f41
%if 0%{?fedora_version} < 43
sed -i 's/license = "MIT"/license = { text = "MIT" }/g' pyproject.toml
sed -i '/license-files/d' pyproject.toml
%endif

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pystitch


%check
%pyproject_check_import
%{py3_test_envvars} %{python3} -m unittest discover test

%files -n python3-pystitch -f %{pyproject_files}


%changelog
%autochangelog
