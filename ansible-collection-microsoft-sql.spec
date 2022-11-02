%bcond_with collection_artifact

Name: ansible-collection-microsoft-sql
Url: https://github.com/linux-system-roles/mssql
Summary: The Ansible collection for Microsoft SQL Server management
Version: 1.2.4
Release: 3%{?dist}

License: MIT

%global rolename mssql
%global collection_namespace microsoft
%global collection_name sql
%global collection_rolename server
%global legacy_rolename %{collection_namespace}.sql-server

%global _pkglicensedir %{_licensedir}/%{name}

Requires: linux-system-roles

%global mainid cdc706f14614ef5e80bbce8db10beb369e889df9
%global parenturl https://github.com/linux-system-roles
Source: %{parenturl}/auto-maintenance/archive/%{mainid}/auto-maintenance-%{mainid}.tar.gz
Source1: %{parenturl}/%{rolename}/archive/%{version}/%{rolename}-%{version}.tar.gz

BuildArch: noarch

# Requirement for %%ansible_collection_build, %%ansible_collection_install, %%ansible_collection_files
BuildRequires: ansible-packaging

# Requirements for md2html.sh to build the documentation
BuildRequires: rubygem-kramdown-parser-gfm

# Requirements for galaxy_transform.py
BuildRequires: python3
BuildRequires: %{py3_dist ruamel.yaml}

%description
This RPM installs the %{collection_namespace}.%{collection_name} Ansible
collection that provides the %{collection_rolename} role for Microsoft SQL
Server management. This RPM also installs the %{legacy_rolename} role
in the legacy roles format for users of Ansible < 2.9.

%if %{with collection_artifact}
%package collection-artifact
Summary: Collection artifact to import to Automation Hub / Ansible Galaxy

%description collection-artifact
Collection artifact for %{name}. This package contains
%{collection_namespace}-%{collection_name}-%{version}.tar.gz
%endif

%prep
%setup -q -a1 -n auto-maintenance-%{mainid}

mv %{rolename}-%{version} %{rolename}

# Remove symlinks in tests/roles
if [ -d %{rolename}/tests/roles ]; then
    find %{rolename}/tests/roles -type l -exec rm {} \;
    if [ -d %{rolename}/tests/roles/linux-system-roles.%{rolename} ]; then
        rm -r %{rolename}/tests/roles/linux-system-roles.%{rolename}
    fi
fi

%build
# Convert README.md to README.html in the source roles
sh md2html.sh %{rolename}/README.md

mkdir .collections
# Copy README.md for the collection build
cp %{rolename}/.collection/README.md lsr_role2collection/collection_readme.md
# Copy galaxy.yml for the collection build
cp %{rolename}/.collection/galaxy.yml ./

# Ensure the correct entries in galaxy.yml
./galaxy_transform.py "%{collection_namespace}" "%{collection_name}" "%{version}" \
                      "Ansible collection for Microsoft SQL Server management" \
                      > galaxy.yml.tmp
mv galaxy.yml.tmp galaxy.yml

# Convert roles to the collection format
python3 lsr_role2collection.py --role "%{rolename}" \
    --src-path "%{rolename}" \
    --src-owner linux-system-roles \
    --dest-path .collections \
    --readme lsr_role2collection/collection_readme.md \
    --namespace %{collection_namespace} \
    --collection %{collection_name} \
    --new-role "%{collection_rolename}" \
    --meta-runtime lsr_role2collection/runtime.yml

# Remove dot files/dirs
rm -r .collections/ansible_collections/%{collection_namespace}/%{collection_name}/.[A-Za-z]*
rm -r .collections/ansible_collections/%{collection_namespace}/%{collection_name}/tests/%{collection_rolename}/.[A-Za-z]*

# Copy galaxy.yml to the collection directory
cp -p galaxy.yml .collections/ansible_collections/%{collection_namespace}/%{collection_name}

# Copy CHANGELOG.md from %%{rolename} to collection dir
mv .collections/ansible_collections/%{collection_namespace}/%{collection_name}/roles/%{collection_rolename}/CHANGELOG.md \
    .collections/ansible_collections/%{collection_namespace}/%{collection_name}/

# Build collection
pushd .collections/ansible_collections/%{collection_namespace}/%{collection_name}/
%ansible_collection_build
popd

%install
mkdir -p %{buildroot}%{ansible_roles_dir}

# Copy role in legacy format and rename rolename in tests
cp -pR %{rolename} "%{buildroot}%{ansible_roles_dir}/%{legacy_rolename}"
sed -i "s/linux-system-roles\.%{rolename}/%{legacy_rolename}/g" \
    %{buildroot}%{ansible_roles_dir}/%{legacy_rolename}/tests/*.yml

# Copy README, COPYING, and LICENSE files to the corresponding directories
mkdir -p %{buildroot}%{_pkglicensedir}
mkdir -p "%{buildroot}%{_pkgdocdir}/%{legacy_rolename}"
cp -p "%{buildroot}%{ansible_roles_dir}/%{legacy_rolename}/README.md" \
    "%{buildroot}%{_pkgdocdir}/%{legacy_rolename}"
cp -p "%{buildroot}%{ansible_roles_dir}/%{legacy_rolename}/README.html" \
    "%{buildroot}%{_pkgdocdir}/%{legacy_rolename}"
if [ -f "%{buildroot}%{ansible_roles_dir}/%{legacy_rolename}/COPYING" ]; then
    cp -p "%{buildroot}%{ansible_roles_dir}/%{legacy_rolename}/COPYING" \
        "%{buildroot}%{_pkglicensedir}/%{legacy_rolename}.COPYING"
fi
if [ -f "%{buildroot}%{ansible_roles_dir}/%{legacy_rolename}/LICENSE" ]; then
    cp -p "%{buildroot}%{ansible_roles_dir}/%{legacy_rolename}/LICENSE" \
        "%{buildroot}%{_pkglicensedir}/%{legacy_rolename}.LICENSE"
fi

# Remove dot files
rm -r %{buildroot}%{ansible_roles_dir}/*/.[A-Za-z]*
rm -r %{buildroot}%{ansible_roles_dir}/%{legacy_rolename}/tests/.[A-Za-z]*

# Remove the molecule directory
rm -r %{buildroot}%{ansible_roles_dir}/*/molecule

# Install collection
pushd .collections/ansible_collections/%{collection_namespace}/%{collection_name}/
%ansible_collection_install
popd

mkdir -p %{buildroot}%{_pkgdocdir}/collection/roles

# Copy the collection README files to the collection
cp -p %{buildroot}%{ansible_collection_files}%{collection_name}/README.md \
   %{buildroot}%{_pkgdocdir}/collection

# Copy role's readme to /usr/share/doc/
if [ -f "%{buildroot}%{ansible_collection_files}%{collection_name}/roles/%{collection_rolename}/README.md" ]; then
    mkdir -p %{buildroot}%{_pkgdocdir}/collection/roles/%{collection_rolename}
    cp -p %{buildroot}%{ansible_collection_files}%{collection_name}/roles/%{collection_rolename}/README.md \
        %{buildroot}%{_pkgdocdir}/collection/roles/%{collection_rolename}
fi

# Convert README.md to README.html for collection in %%{buildroot}%%{_pkgdocdir}/collection
sh md2html.sh %{buildroot}%{_pkgdocdir}/collection/roles/%{collection_rolename}/README.md

%if %{with collection_artifact}
# Copy collection artifact to /usr/share/ansible/collections/ for collection-artifact
pushd .collections/ansible_collections/%{collection_namespace}/%{collection_name}/
if [ -f %{collection_namespace}-%{collection_name}-%{version}.tar.gz ]; then
    mv %{collection_namespace}-%{collection_name}-%{version}.tar.gz \
       %{buildroot}%{_datadir}/ansible/collections/
fi
popd
%endif

%files -f %{ansible_collection_filelist}
%{_pkgdocdir}
%license %{_pkglicensedir}
%{ansible_roles_dir}/%{legacy_rolename}

%if %{with collection_artifact}
%files collection-artifact
%{_datadir}/ansible/collections/%{collection_namespace}-%{collection_name}-%{version}.tar.gz
%endif

%changelog
* Thu Sep 22 2022 Sergei Petrosian <spetrosi@redhat.com> - 1.2.4-3
- Further simplify spec file
  - Do not install roles to /usr/share/microsoft and then create symlinks
    to /usr/share/ansible/roles/, instead install directly to
    /usr/share/ansible/roles/
  - Remove unused removal of ambiguous python shebangs

* Tue Sep 20 2022 Sergei Petrosian <spetrosi@redhat.com> - 1.2.4-2
- Remove all code unrelated to Fedora to siplify the file
  - Remove bcond_with ansible because Fedora always have ansible
  - Replace the ansible_build_dep macro with simple ansible-packaging
  - Remove %%bcond_with html because Fedora always can convert md to html
  - Remove conditions related to RHEL
  - Replace ansible_collection_build_install with biult-in build & install
  - Remove unrelated to Fedora Provides
  - Remove all loops because this RPM contains only one role
  - Remove definition of ansible_collection_files as its part of ansible-packaging
  - Clean up %%files section
    - Use ansible_collection_files in %%files section
    - Remove duplicated lines and wildcards
  - Remove defsource - simply define the source for mssql
  - Escape macros in comments with a second %
  - 's|$RPM_BUILD_ROOT|%%{buildroot}|' for consistency
  -  Remove getarchivedir for simplicity
  - Wrap description by 80 symbols and clarify it
  - Remove tests/.fmf dir from the RPM
  Resolves: rhbz#2126901

* Thu Sep 1 2022 Sergei Petrosian <spetrosi@redhat.com> - 1.2.4-1
- Replicate all provided databases
  - This change fixes the bug where only the first database provided with
mssql_ha_db_names got replicated
  - Clarify that the role does not remove not listed databases
  Resolves: rhbz#2066337
- Input multiple sql scripts
  - Allow _input_sql_file vars to accept list of files
  - Flush handlers prior to inputting post sql script
  Resolves: rhbz#2120712
- Note that ha_cluster is not idempotent
- SPEC: Do not update dates in CHANGELOG.md

* Thu Aug 25 2022 Sergei Petrosian <spetrosi@redhat.com> - 1.2.3-1
- Use firewall role to configure firewall for SQL Server
  Resolves: rhbz#2120709
- Add mssql_ha_virtual_ip
  Replace mssql_ha_db_name with mssql_ha_db_names to let users replicate multiple DBs
  Resolves: rhbz#2066337

- Replace simple `mssql_input_sql_file` with `pre` and `post` variables
  Resolves: rhbz#2120712
- Add Requires: linux-system-roles or rhel-system-roles
- Replace fedora.linux_system_roles:redhat.rhel_system_roles on RHEL
- Add downstream values to galaxy.yml
- Change defcommit to defsource that takes both tags and commits
- Update CHANGELOG.md with the current date and copy it to collection dir

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 21 2022 Sergei Petrosian <spetrosi@redhat.com> - 1.1.1-3
- Fix inserting ansible_managed
  Resolves: rhbz#2057651 (EL8)
  Resolves: rhbz#2064690 (EL9)
- Users now can provide a custom URLs to pull packages and RPM key from
  Resolves: rhbz#2038256 (EL8)
  Resolves: rhbz#2064648 (EL9)

* Fri Mar 18 2022 Sergei Petrosian <spetrosi@redhat.com> - 1.1.1-2
- RHEL8.6, 9 - add "Requires: ansible-core or ansible"
  Resolves: rhbz#2065664 (EL8)
  Resolves: rhbz#2065669 (EL8)

* Thu Mar 17 2022 Sergei Petrosian <spetrosi@redhat.com> - 1.1.1-1
- Insert the "Ansible managed" comment to the /var/opt/mssql/mssql.conf file
  Resolves rhbz#2057651 (EL8)
  Resolves rhbz#2064690 (EL9)

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 21 2021 Sergei Petrosian <spetrosi@redhat.com> - 1.1.0-1
- Add support for Microsoft SQL Server 2017

* Mon Jul 19 2021 Sergei Petrosian <spetrosi@redhat.com> - 1.0.12-2
- Copy fix for RHEL 7 builds from rhel-system-roles
  Link to the original fix:
  https://src.fedoraproject.org/rpms/linux-system-roles/c/093981119f99ac51a6e06a2714b587e4e2fe287c

* Tue Jul 13 2021 Sergei Petrosian <spetrosi@redhat.com> - 1.0.12-1
- Add the meta-runtime option from the latest auto-maintenance
- Use the latest mssql that ships fixes for issues #24,#25,#26,#27,#28,35

* Tue Jun 29 2021 Sergei Petrosian <spetrosi@redhat.com> - 1.0.11-3
- Add a missing slash at the {ansible_collection_files} definition for rhel 7

* Thu Jun 17 2021 Sergei Petrosian <spetrosi@redhat.com> - 1.0.11-2
- Make the ansible_collection_files macro defined in Fedora automatically and
  in RHEL manually consistent - having slash at the end to clean double-slashes

* Thu Jun 17 2021 Sergei Petrosian <spetrosi@redhat.com> - 1.0.11-1
- Update the version to be consistent with the Galaxy collection at
  https://galaxy.ansible.com/microsoft/sql

* Wed Jun 16 2021 Sergei Petrosian <spetrosi@redhat.com> - 0.0.1-5
- Update commit hash for mssql

* Wed Jun 16 2021 Sergei Petrosian <spetrosi@redhat.com> - 0.0.1-4
- Generate symlinks for roles in /usr/share/ansible/roles

* Wed Jun 16 2021 Sergei Petrosian <spetrosi@redhat.com> - 0.0.1-3
- Copy changes made to linux-system-roles in this PR:
  https://src.fedoraproject.org/rpms/linux-system-roles/pull-request/13#
- Make spec file available for older versions of OSes.
- Drop python3-six dependency which was used by lsr_role2collection.py.
- Drop html files from rpm if the version has no markdown parser.
- Drop unnecessary python scripts which include python3 only code, e.g.,
  f-strings.
  Resolves rhbz#1970165

* Mon Jun 14 2021 Sergei Petrosian <spetrosi@redhat.com> - 0.0.1-2
- Fix long description lines
- Fix incorrect role includes in microsoft/sql-server/tests/

* Thu Jun 3 2021 Sergei Petrosian <spetrosi@redhat.com> - 0.0.1-1
- Initial release
