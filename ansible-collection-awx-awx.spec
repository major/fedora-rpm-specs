# ansible-core is built for alternative Python stacks in RHEL which do not have
# the necessary test deps packaged.
Name:		ansible-collection-awx-awx
Version:	23.2.0
Release:	1%{?dist}
Summary:	Ansible modules and plugins for working with AWX

License:	GPL-3.0-or-later AND BSD-2-Clause
URL:		%{ansible_collection_url awx awx}
Source0:	https://github.com/ansible/awx/archive/%{version}/awx-%{version}.tar.gz
# This patch is removing the following files / folders:
# - Test & Tests: remove any unnecessary test files that we are not uising at
#   this time.
# - images: No need to have an image of the completed test in the collection RPM.
# - Testing.md: Removed instructions for building and testing the collection.
# Files used for Execution build and python requirements
# - requirements.txt
# - bindep.txt
# We install these files with the license and doc section. We don't want them duplicated.
# - COPYING
# - README
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
* Tue Oct 03 2023 Andrew H <aheath1992@gmail.com> - 23.2.0-1
- Update to 23.2.0.

* Fri Sep 15 2023 Andrew H <aheath1992@gmail.com> - 23.1.0-1
- Update to 23.1.0.

* Tue Aug 29 2023 Andrew H <aheath1992@gmail.com> - 23.0.0-1
- Update to 23.0.0.

* Wed Aug 23 2023 Andrew H <aheath1992@gmail.com> - 22.7.0-1
- Update to 22.7.0.

* Fri Jul 28 2023 Andrew H <aheath1992@gmail.com> - 22.6.0-1
- Initial Package
