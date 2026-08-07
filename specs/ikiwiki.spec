Name:           ikiwiki
Version:        3.20260201
Release:        %autorelease
Summary:        A wiki compiler

# ikiwiki is licensed under GPLv2+, the Python code in plugins/ under
# BSD (2-clause)
# SPDX
License:        GPL-2.0-or-later AND BSD-2-Clause
URL:            https://ikiwiki.info/
Source0:        https://ftp.debian.org/debian/pool/main/i/%{name}/%{name}_%{version}.orig.tar.xz
Patch0:         ikiwiki-libexecdir.patch
# Correct t/git.t test
Patch1:         ikiwiki-fakehome.patch
Patch2:         ikiwiki-proxy_py.patch
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  gettext
BuildRequires:  findutils
BuildRequires:  make
%if 0%{?rhel} && 0%{?rhel} < 7
BuildRequires:  perl
%else
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
%endif
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(lib)
# ikiwiki.in loads IkiWiki, IkiWiki::CGI, IkiWiki::Render, IkiWiki::Setup,
# and IkiWiki::Wrapper.
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(CGI::FormBuilder) >= 3.02.02
BuildRequires:  perl(CGI::Session)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::MimeInfo)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::ReadBackwards)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTML::Scrubber)
BuildRequires:  perl(HTML::Tagset)
BuildRequires:  perl(HTML::Template)
BuildRequires:  perl(Image::Magick)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(Locale::Po4a::Chooser)
BuildRequires:  perl(Locale::Po4a::Po)
BuildRequires:  perl(Mail::Sendmail)
BuildRequires:  perl(Memoize)
# Monotone not used at tests
# Net::Amazon::S3 not used at tests
BuildRequires:  perl(open)
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(RPC::XML)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(Term::ReadLine)
# Text::MultiMarkdown || Text::Markdown::Discount || Text::Markdown || Markdown
# || /usr/bin/markdown
BuildRequires:  perl(Text::Markdown)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
%if ! 0%{?rhel}
BuildRequires:  perl(XML::Feed)
%endif
BuildRequires:  perl(XML::SAX)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(YAML::XS)
# Optional run-time:
# Locale::gettext not used at tests
%if ! 0%{?rhel}
BuildRequires:  perl(Net::OpenID::VerifiedIdentity)
%endif
# UUID::Tiny not used at tests
# Tests:
BuildRequires:  perl(B)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  bzr
BuildRequires:  cvs
BuildRequires:  cvsps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  mercurial
BuildRequires:  perl(HTML::LinkExtor)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(XML::Twig)
BuildRequires:  python%{python3_pkgversion}-docutils
BuildRequires:  subversion

Requires:       perl(CGI::FormBuilder) >= 3.02.02
Requires:       perl(CGI::Session)
Requires:       perl(Digest::SHA)
Requires:       perl(HTML::Scrubber)
Requires:       perl(Image::Magick)
Requires:       perl(Mail::Sendmail)
Requires:       perl(Sys::Syslog)
Requires:       perl(Text::Markdown)
%if ! 0%{?rhel}
Requires:       perl(XML::Feed)
%endif
Requires:       perl(XML::Simple)
Requires:       perl(YAML::XS)

%if "%{?python3_version}" != ""
Requires:       python(abi) = %{python3_version}
%endif
Requires:       python%{python3_pkgversion}-docutils

# IkiWiki package spreads over more files. Provide the file names as modules
# because they are loaded in that way.
Provides:       perl(IkiWiki::Render)
Provides:       perl(IkiWiki::UserInfo)

%global cgi_bin %{_libexecdir}/w3m/cgi-bin

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(IkiWiki\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(IkiWiki\\)$

%description
Ikiwiki is a wiki compiler. It converts wiki pages into HTML pages
suitable for publishing on a website. Ikiwiki stores pages and history
in a revision control system such as Subversion or Git. There are many
other features, including support for blogging, as well as a large
array of plugins.


%prep
%setup -q -n ikiwiki-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

# goes into the -w3m subpackage
cat << \EOF > README.fedora
See http://ikiwiki.info/w3mmode/ for more information.
EOF

# Drop Monotone plugin
# Monotone depends on botan v1, which has been EOL for a long time
rm -v IkiWiki/Plugin/monotone.pm


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix}
# parallel builds currently don't work
make


%check
make test || :


%install
make pure_install DESTDIR=%{buildroot} W3M_CGI_BIN=%{cgi_bin}
%find_lang %{name}

# move external plugins
mkdir -p %{buildroot}%{_libexecdir}/ikiwiki/plugins
mv %{buildroot}%{_prefix}/lib/ikiwiki/plugins/* \
   %{buildroot}%{_libexecdir}/ikiwiki/plugins

# remove shebang
sed -e '1{/^#!/d}' -i \
    %{buildroot}%{_sysconfdir}/ikiwiki/auto.setup \
    %{buildroot}%{_sysconfdir}/ikiwiki/auto-blog.setup \
    %{buildroot}%{_libexecdir}/ikiwiki/plugins/proxy.py \
    %{buildroot}%{_libexecdir}/ikiwiki/plugins/rst

# fix shebang
sed -e '1i#!%{__python3}' -i \
    %{buildroot}%{_libexecdir}/ikiwiki/plugins/rst

# fix permissions
find %{buildroot}%{perl_vendorlib}/IkiWiki -type f \
     -exec chmod -x {} \;

# https://fedoraproject.org/wiki/Changes/Unify_bin_and_sbin
%if 0%{?fedora} >= 42
mv %{buildroot}%{_prefix}/sbin/ikiwiki-mass-rebuild \
   %{buildroot}%{_sbindir}
%endif


%files -f %{name}.lang
%{_bindir}/ikiwiki
%{_bindir}/ikiwiki-calendar
%{_bindir}/ikiwiki-comment
%{_bindir}/ikiwiki-makerepo
%{_bindir}/ikiwiki-transition
%{_bindir}/ikiwiki-update-wikilist
%{_sbindir}/ikiwiki-mass-rebuild
%{_mandir}/man1/ikiwiki*
%{_mandir}/man8/ikiwiki*
%{_mandir}/man3/IkiWiki*
%{_datadir}/ikiwiki
%dir %{_sysconfdir}/ikiwiki
%config(noreplace) %{_sysconfdir}/ikiwiki/*
# contains a packlist only
%exclude %{perl_vendorarch}
%{perl_vendorlib}/IkiWiki*
%exclude %{perl_vendorlib}/IkiWiki*/Plugin/skeleton.pm.example
%if 0%{?rhel}
# disable the S3 plugin for now, as perl-Net-Amazon-S3 is not
# available on epel6 (rhbz#1125850)
%exclude %{perl_vendorlib}/IkiWiki*/Plugin/amazon_s3.pm
%endif
%{_libexecdir}/ikiwiki
%doc README debian/changelog debian/NEWS html
%doc IkiWiki/Plugin/skeleton.pm.example
%if 0%{?_licensedir:1}
# include license file a second time
%license html/GPL
%endif


%package w3m
Summary:        Ikiwiki w3m cgi meta-wrapper
Requires:       w3m
Requires:       %{name} = %{version}-%{release}

%description w3m
Enable usage of all of ikiwiki's web features (page editing, etc) in
the w3m web browser without a web server. w3m supports local CGI
scripts, and ikiwiki can be set up to run that way using the
meta-wrapper in this package.


%files w3m
%doc README.fedora
%{cgi_bin}/ikiwiki-w3m.cgi


%changelog
%autochangelog
