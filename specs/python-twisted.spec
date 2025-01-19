%global srcname twisted

%global common_description %{expand:
Twisted is a networking engine written in Python, supporting numerous protocols.
It contains a web server, numerous chat clients, chat servers, mail servers
and more.}

Name:           python-%{srcname}
Version:        24.10.0
Release:        %autorelease
Summary:        Twisted is a networking engine written in Python

License:        MIT
URL:            http://twistedmatrix.com/
VCS:            https://github.com/twisted/twisted
Source0:        %vcs/archive/%{srcname}-%{version}/%{srcname}-%{version}.tar.gz
# downstream-only disable tests that fail in the buildsystem or due to sha1
Patch0:         python-twisted-24.10.0-disable-tests.patch

BuildArch:      noarch

%description %{common_description}

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  git-core
BuildRequires:  python3-bcrypt
BuildRequires:  python3-cryptography
BuildRequires:  python3-devel >= 3.3
BuildRequires:  python3-h2
BuildRequires:  python3-hamcrest
BuildRequires:  python3-httpx
BuildRequires:  python3-hypothesis
BuildRequires:  python3-pyasn1-modules
BuildRequires:  python3-pynacl
BuildRequires:  python3-pyOpenSSL
BuildRequires:  python3-service-identity
BuildRequires:  python3-subunit

Recommends:  python3-%{srcname}+tls

%description -n python3-%{srcname} %{common_description}

%pyproject_extras_subpkg -n python3-%{srcname} tls


%prep
%autosetup -p1 -n %{srcname}-%{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

# no-manual-page-for-binary
mkdir -p %{buildroot}%{_mandir}/man1/
for s in conch core mail; do
cp -a docs/$s/man/*.1 %{buildroot}%{_mandir}/man1/
done

# Packages that install arch-independent twisted plugins install here.
# https:# bugzilla.redhat.com/show_bug.cgi?id=1252140
mkdir -p %{buildroot}%{python3_sitelib}/twisted/plugins

# Move and symlink python3 scripts
ln -s ./trial %{buildroot}%{_bindir}/trial-3
ln -s ./twistd %{buildroot}%{_bindir}/twistd-3

%pyproject_save_files %{srcname}
echo "%ghost %{python3_sitelib}/twisted/plugins/dropin.cache" >> %{pyproject_files}


%check
PATH=%{buildroot}%{_bindir}:$PATH PYTHONPATH=$PWD/src %{buildroot}%{_bindir}/trial twisted


%files -n python3-twisted  -f %{pyproject_files}
%doc NEWS.rst README.rst
%license LICENSE
%{_bindir}/cftp
%{_bindir}/ckeygen
%{_bindir}/conch
%{_bindir}/mailmail
%{_bindir}/pyhtmlizer
%{_bindir}/tkconch
%{_bindir}/trial
%{_bindir}/twist
%{_bindir}/twistd
%{_bindir}/trial-3
%{_bindir}/twistd-3
%{_mandir}/man1/cftp.1*
%{_mandir}/man1/ckeygen.1*
%{_mandir}/man1/conch.1*
%{_mandir}/man1/mailmail.1*
%{_mandir}/man1/pyhtmlizer.1*
%{_mandir}/man1/tkconch.1*
%{_mandir}/man1/trial.1*
%{_mandir}/man1/twistd.1*


%changelog
%autochangelog
