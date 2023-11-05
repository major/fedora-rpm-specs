%global forgeurl https://github.com/mailprocessing/mailprocessing

%global _description %{expand:
The mailprocessing library contains two executables: maildirproc and
imapproc. maildirproc processes one or several several existing mail
boxes in the maildir format. It is primarily focused on mail sorting -
i.e., moving, copying, forwarding and deleting mail according to a set
of rules. It can be seen as an alternative to procmail, but instead of
being a delivery agent (which wants to be part of the delivery chain),
maildirproc only processes already delivered mail. And that's a
feature, not a bug. imapproc does the same thing for IMAP folders.}

Name:           mailprocessing
Version:        1.2.7
Release:        %autorelease
Summary:        Maildir and IMAP processor/filter
%global tag %{version}
%forgemeta
License:        GPL-2.0-only
URL:            %forgeurl
Source0:        %forgesource
# Fixes rpmlint incorrect-fsf-address error
# Patch from https://github.com/mailprocessing/mailprocessing/pull/14
Patch0:         fix-incorrect-fsf-address.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  make
BuildRequires:  git-core

Obsoletes:      maildirproc < 1.0.2
Provides:       maildirproc = %{version}-%{release}


%description %_description


%prep
%forgeautosetup -p1 -S git


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
pushd docs
  make
popd


%install
%pyproject_install
%pyproject_save_files %{name}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man5
mv docs/*proc.1 %{buildroot}%{_mandir}/man1/
mv docs/%{name}.5 %{buildroot}%{_mandir}/man5/


%files -n %{name} -f %{pyproject_files}
%doc NEWS README
%doc docs/*html docs/*rst docs/examples docs/reference
%{_bindir}/imapproc
%{_bindir}/maildirproc
%{_mandir}/man1/*proc.1*
%{_mandir}/man5/%{name}*


%changelog
%autochangelog
