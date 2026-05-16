Name:           ansible-collection-chocolatey-chocolatey
Version:        1.6.0
Release:        %autorelease
Summary:        Ansible collection for Chocolatey

License:        GPL-3.0-or-later
URL:            %{ansible_collection_url chocolatey chocolatey}
Source:         https://github.com/chocolatey/chocolatey-ansible/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ansible-packaging

BuildArch:      noarch

%description
The collection includes the modules required to configure Chocolatey, as well
as manage packages on Windows using Chocolatey.

%prep
%autosetup -n chocolatey-ansible-%{version}
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
sed -i -e 's/{{ REPLACE_VERSION }}/%{version}/' chocolatey/galaxy.yml
cat >> chocolatey/galaxy.yml << EOF
build_ignore:
  # Remove unnecessary development files from the built package.
  - tests
  - azure-pipelines.yml
  - .gitignore
  # Licenses and docs are installed with %%doc and %%license
  - LICENSE
  - README.md
EOF

%build
cd chocolatey
%ansible_collection_build

%install
cd chocolatey
%ansible_collection_install

# No unit tests

%files -f %{ansible_collection_filelist}
%license LICENSE
%doc README.md

%changelog
%autochangelog
