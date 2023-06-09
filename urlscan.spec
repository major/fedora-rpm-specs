Name:           urlscan
Version:        1.0.0
Release:        %autorelease
Summary:        Extract and browse the URLs contained in an email (urlview replacement)

License:        GPLv2+
URL:            https://github.com/firecat53/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        muttrc

BuildArch:      noarch
BuildRequires:  python3-devel


%description
%{name} searches for URLs in email messages, then displays a list of them in
the current terminal. It is primarily meant as a replacement for urlview.


%prep
%autosetup
cp -p %{SOURCE1} .

# stop installing LICENSE file in docdir
sed -i '/^LICENSE/ d' pyproject.toml

# remove shebang
sed -i '/\/usr\/bin\/env.*python/ d' urlscan/__main__.py

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires


%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel


%install
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_install
%pyproject_save_files urlscan

# remove extra file
rm -fr %{buildroot}/%{_docdir}/%{name}/


%files -f %{pyproject_files}
%doc muttrc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
%autochangelog
