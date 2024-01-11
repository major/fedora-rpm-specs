Name:       git-autofixup
Version:    0.004006
Release:    %autorelease

Summary:    Autofixup - create fixup commits for topic branches

License:    Artistic-2.0
URL:        https://github.com/torbiak/git-autofixup/
Source0:    https://cpan.metacpan.org/authors/id/T/TO/TORBIAK/App-Git-Autofixup-%{version}.tar.gz

BuildArch:  noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl-macros
BuildRequires:  perl(:VERSION) >= 5.8.4
# Build
BuildRequires:  /usr/bin/make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test
BuildRequires:  git-core
BuildRequires:  perl(Cwd)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)

# The plugins needs only the basic functionalities of git
# git requires git-core so all users with git or git-all have it
Requires:       git-core

%description
git-autofixup parses hunks of changes in the working directory out of \
git diff output and uses git blame to assign those hunks to commits in \
<revision>..HEAD, which will typically represent a topic branch, and then \
creates fixup commits to be used with git rebase --interactive --autosquash. \
It is assumed that hunks near changes that were previously committed to \
the topic branch are related.


%prep
%setup -q -n App-Git-Autofixup-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*

%check
git config --global init.defaultBranch master
make test

%files
%doc Changes README.pod
%license LICENSE
%{_bindir}/git-autofixup
%{_mandir}/man1/git-autofixup.1*
%{_mandir}/man3/App::Git::Autofixup.3pm*
%{perl_vendorlib}/*

%changelog
%autochangelog
