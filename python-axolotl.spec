Name:           python-axolotl
Version:        0.2.3
Release:        %autorelease
Summary:        Python port of libaxolotl

License:        GPL-3.0-only
URL:            https://github.com/tgalal/python-axolotl
Source0:        %{url}/archive/%{version}/%{version}.tar.gz

# The protobuf dependency is too strict, this patch relaxes the requirement
# https://github.com/tgalal/python-axolotl/issues/44
Patch0:         python-axolotl-protobuf.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This is a ratcheting forward secrecy protocol
that works in synchronous and asynchronous messaging environments.}

%description %_description

%package -n python3-axolotl
Summary:        %{summary}

%description -n python3-axolotl %_description


%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files axolotl


%check
%tox


%files -n python3-axolotl -f %{pyproject_files}
%doc README.md
%license LICENSE


%changelog
%autochangelog
