Name:           python-axolotl
Version:        0.2.3
Release:        3%{?dist}
Summary:        Python port of libaxolotl

License:        GPLv3
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
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.2.3-2
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Arthur Bols <arthur@bols.dev> - 0.2.3-1
- Initial package

