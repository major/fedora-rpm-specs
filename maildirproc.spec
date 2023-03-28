%global pypi_name maildirproc

%global _description %{expand:
maildirproc is a program that processes one or several existing mail boxes in
the maildir format. It is primarily focused on mail sorting, which means
moving, copying, forwarding, and deleting mail according to a set of rules.
It can be seen as an alternative to procmail, but instead of being a delivery
agent (which wants to be part of the delivery chain), maildirproc only
processes mail which has already been delivered. That is a feature, not a bug.}

Name:           %{pypi_name}
Version:        1.0.1
Release:        %autorelease
Summary:        Sort mail from mail boxes in the maildir format

License:        GPL-2.0-or-later
URL:            http://joel.rosdahl.net/maildirproc/
Source0:        https://files.pythonhosted.org/packages/source/m/%{name}/%{name}-%{version}a.tar.bz2

BuildArch:      noarch
BuildRequires:  python3-devel

%description %_description


%prep
%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install


%files
%license LICENSE
%doc NEWS README doc/*
%{_bindir}/%{name}
%{python3_sitelib}/%{name}-%{version}*/

%changelog
%autochangelog
