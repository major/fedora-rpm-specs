# ansible-core is built for alternative Python stacks in RHEL which do not have
# the necessary test deps packaged.
Name:		ansible-collection-awx-awx
Version:	23.6.0
Release:	%autorelease
Summary:	Ansible modules and plugins for working with AWX

License:	GPL-3.0-or-later AND BSD-2-Clause
URL:		%{ansible_collection_url awx awx}
Source0:	https://github.com/ansible/awx/archive/%{version}/awx-%{version}.tar.gz
Patch0:		build_ignore-unnecessary-files.patch

BuildArch:	noarch

BuildRequires:	ansible-packaging

%description
ansible-collection-awx-awx provides the Awx.Awx Ansible
collection. The collection includes Ansible modules and plugins for working
with AWX.

%prep
%autosetup -n awx-%{version} -p1
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

%build
ansible-playbook -i localhost, awx_collection/tools/template_galaxy.yml \
	  -e collection_package=awx \
	  -e collection_namespace=awx \
	  -e collection_version=%{version} \
	  -e '{"awx_template_version": false}'
cd awx_collection_build/
%ansible_collection_build

%install
cd awx_collection_build/
%ansible_collection_install

%files -f %{ansible_collection_filelist}
%license awx_collection_build/COPYING
%doc awx_collection_build/README.md

%changelog
%autochangelog
