%bcond_without check
# Some tests use a package that uses this.
%bcond_with bootstrap

# The output from a standard Hugo package build can be overwhelming when
# trying to diagnose package build errors. A less verbose follow up
# is:
#
# 1. Run "rpmbuild -ba hugo.spec >/tmp/LOG 2>&1" to capture all of
# the output.
#
# 2. Look for the command "go build ..." in that output.
#
# 3. Enter the BUILD/hugo-VERSION directory.
#
# 4. Export the two variables set before "go build ...".
#
# 5. Run the "go build ..." command, but without the "-v" and "-x".

# https://github.com/gohugoio/hugo
%global goipath github.com/gohugoio/hugo
Version:        0.140.2

%gometa -f

%global common_description %{expand:
Hugo is a static HTML and CSS website generator written in Go. It is optimized
for speed, easy use and configurability. Hugo takes a directory with content
and templates and renders them into a full HTML website.}

%global golicenses      LICENSE docs/LICENSE.md docs/themes/gohugoioTheme/license.md
%global godocs          docs examples README.md CONTRIBUTING.md

Name:           hugo
Release:        %autorelease
Summary:        The world’s fastest framework for building websites

# Upstream license specification: Apache-2.0 and MIT
License:        Apache-2.0 AND MIT
URL:            %{gourl}
Source0:        %{gosource}
# Skip tests that uses the network.
# Based on https://sources.debian.org/data/main/h/hugo/0.58.3-1/debian/patches/0005-skip-modules-TestClient.patch
Patch0001:      0010-skip-modules-TestClient.patch
# Fix build on Go 1.24.
# Submitted upstream as https://github.com/gohugoio/hugo/pull/13285
Patch0002:      0020-remove-non-const-fmt-string.patch

BuildRequires:  golang(github.com/bep/golibsass/libsass) >= 0.7.0
BuildRequires:  golang-github-gohugoio-hugo-goldmark-extensions-devel

# This is in response to Red Hat Bugzilla #2104346. The full dependencies
# for Hugo are large, including GCC and the Go toolchain. For example,
# "hugo server" will not work without these. It might be beneficial to avoid
# such large dependencies in some instances---such as CI pipelines---that
# do not require "hugo server". Thus golang-bin is a weak dependency.
#
# Also see the discussion at https://src.fedoraproject.org/rpms/hugo/pull-request/13.
Recommends:     golang-bin

%description
%{common_description}

%gopkg

%prep
%goprep

# See https://github.com/gohugoio/hugo/issues/9860
sed -i 's|github.com/clbanning/mxj/v2|github.com/clbanning/mxj|' $(find . -iname '*.go' -type f)

# See https://github.com/gohugoio/hugo/issues/9860
# and https://github.com/nicksnyder/go-i18n/pull/253
# and https://bugzilla.redhat.com/show_bug.cgi?id=2031583
sed -i 's|github.com/gohugoio/go-i18n/v2|github.com/nicksnyder/go-i18n/v2|' $(find . -iname '*.go' -type f)

%autopatch -p1

# Replace blackfriday import path to avoid conflict with v2
sed -i \
    -e 's|"github.com/russross/blackfriday|"gopkg.in/russross/blackfriday.v1|' \
    $(find . -name '*.go')

# Skip test that assumes directory is in a git repository
sed -i '/TestPageWithLastmodFromGitInfo/a t.Skip()' hugolib/page_test.go

%if %{with bootstrap}
# Delete test using github.com/gohugoio/testmodBuilder/mods which has a
# dependency loop.
rm hugolib/hugo_modules_test.go
%endif

%generate_buildrequires
%go_generate_buildrequires

%build
BUILDTAGS="extended" LDFLAGS="${LDFLAGS} -X %{goipath}/common/hugo.buildDate=$(date --iso=seconds --date=@$SOURCE_DATE_EPOCH) -X %{goipath}/common/hugo.vendorInfo=Fedora:%{version}-%{release}" %gobuild -o %{gobuilddir}/bin/hugo %{goipath}
%{gobuilddir}/bin/hugo completion bash >hugo-completion
%{gobuilddir}/bin/hugo gen man

%install
%gopkginstall

install -d -p %{buildroot}%{_bindir}
install -Dp -m 0755 %{gobuilddir}/bin/hugo %{buildroot}%{_bindir}
install -Dp hugo-completion %{buildroot}%{_datadir}/bash-completion/completions/hugo
install -Dp man/* -t %{buildroot}%{_mandir}/man1

%if %{with check}
%check

# .: Extensive test that uses network.
# cache/dynacache: times out
# hugolib: panic: runtime error: invalid memory address or nil pointer dereference
# hugolib/pagesfromdata: panic: runtime error: invalid memory address or nil pointer dereference
# internal/js/esbuild: binary with name "npm" not found in PATH
# langs/i18n: fails with current Rawhide
# resources/resource_factories/bundler: uses networking
# resources/resource_factories/create: uses networking
# tpl/tplimpl: https://github.com/gohugoio/hugo/issues/13204
%gocheck \
	-d . \
	-d cache/dynacache \
	-d hugolib \
	-d hugolib/pagesfromdata \
	-d internal/js/esbuild \
	-d langs/i18n \
	-d resources/resource_factories/bundler \
	-d resources/resource_factories/create \
	-d tpl/tplimpl \

%endif

%files
%doc CONTRIBUTING.md README.md docs
%license LICENSE
%{_bindir}/hugo
%{_datadir}/bash-completion/completions/hugo
%{_mandir}/man1/*.1*

%gopkgfiles

%changelog
%autochangelog
