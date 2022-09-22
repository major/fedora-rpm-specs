Name:           jo
Summary:        Small utility to create JSON objects
Version:        1.6
Release:        %autorelease

URL:            https://github.com/jpmens/jo
Source0:        %{url}/archive/%{version}/jo-%{version}.tar.gz
# The entire source is GPL-2.0-or-later, except:
#
#   - json.c and json.h are MIT
#   - base64.c and base64.h are LicenseRef-Fedora-Public-Domain: from base64.c,
#     “This code is public domain software.”
#
# See:
# https://docs.fedoraproject.org/en-US/legal/license-field/#_public_domain
# https://docs.fedoraproject.org/en-US/legal/update-existing-packages/#_public_domain
License:        GPL-2.0-or-later AND MIT AND LicenseRef-Fedora-Public-Domain

BuildRequires:  gcc

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake

# Currently, rebuilding jo.md and jo.1 from jo.pandoc does not work for us:
#
#   /usr/bin/pandoc -s -w man+simple_tables -o jo.1 jo.pandoc
#   [WARNING] Could not deduce format from file extension .pandoc
#     Defaulting to markdown
#   The extension simple_tables is not supported for man
#
# We are not required to rebuild these, so for now we just use the ones from
# the source tarball without rebuilding them; we therefore do not BR pandoc.

BuildRequires:  pkgconfig(bash-completion)
%global bashcompdir %(pkg-config --variable=completionsdir bash-completion 2>/dev/null)
BuildRequires:  zsh
%global zshcompdir %{_datadir}/zsh/site-functions
%global zshcomproot %(dirname %{zshcompdir} 2>/dev/null)

# Upstream URL: http://ccodearchive.net/info/json.html
# Upstream VCS: https://github.com/rustyrussell/ccan/tree/master/ccan/json
#
# This is a copylib and not designed to be built as a separate library. See
# https://fedoraproject.org/wiki/Bundled_Libraries_Virtual_Provides; even under
# the old guidelines, in which bundled libraries required FPC exemptions, a
# variety of similar CCAN modules had exemptions as copylibs.
#
# Inspection of https://github.com/rustyrussell/ccan/tree/master/ccan/json
# shows the bundled code is consistent with version 0.1 (as declared in a
# comment in https://github.com/rustyrussell/ccan/blob/master/ccan/json/_info),
# but has been forked with various small modifications in json.c.
Provides:       bundled(ccan-json) = 0.1

# The public-domain base64 implementation looks like a copylib, but I could not
# find the upstream from which it was copied, so I am not treating it as a
# bundled dependency.

%description
This is jo, a small utility to create JSON objects

  $ jo -p name=jo n=17 parser=false
  {
      "name": "jo",
      "n": 17,
      "parser": false
  }

or arrays

  $ seq 1 10 | jo -a
  [1,2,3,4,5,6,7,8,9,10]


%prep
%autosetup


%build
autoreconf -fiv
%configure
%make_build


%install
%make_install


%check
%make_build check


%files
%license COPYING
%doc AUTHORS
%doc ChangeLog
# NEWS not included because it is empty
%doc press.md
%doc README.md
%doc jo.md

%{_bindir}/jo
%{_mandir}/man1/jo.1*

# It is historically standard for packages providing shell completions to
# co-own the completions directory in lieu of having a runtime dependency on
# the relevant shell completions package. However, for bash (but not for other
# shells), this directory and its parent are now owned by the “filesystem”
# package in all current Fedora releases plus EPEL8 and newer.
%{bashcompdir}/jo.bash
%dir %{zshcomproot}
%dir %{zshcompdir}
%{zshcompdir}/_jo


%changelog
%autochangelog
