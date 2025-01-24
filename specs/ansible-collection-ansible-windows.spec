%if %{defined fedora}
%bcond_without tests
%else
%bcond_with tests
%endif

Name:           ansible-collection-ansible-windows
Version:        2.7.0
Release:        %autorelease
Summary:        Windows core collection for Ansible

License:        GPL-3.0-or-later
URL:            %{ansible_collection_url ansible windows}
Source:         https://github.com/ansible-collections/ansible.windows/archive/refs/tags/%{version}.tar.gz
# build_ignore development files, tests, and docs, downstream only
Patch:          build_ignore.patch

BuildArch:      noarch

BuildRequires:  ansible-packaging
%if %{with tests}
BuildRequires:  ansible-packaging-tests
%endif

%description
%{summary}.


%prep
%autosetup -p1 -n ansible.windows-%{version}
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
find . -type f -empty ! -name __init__.py -print -delete


%build
%ansible_collection_build


%install
%ansible_collection_install


%check
%if %{with tests}
%ansible_test_unit
%endif


%files -f %{ansible_collection_filelist}
%license COPYING
%doc README.md CHANGELOG.rst docs/*


%changelog
%autochangelog
