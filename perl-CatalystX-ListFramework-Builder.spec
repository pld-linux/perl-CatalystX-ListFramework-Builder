#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	CatalystX
%define	pnam	ListFramework-Builder
Summary:	CatalystX::ListFramework::Builder - Instant AJAX web front-end for DBIx::Class, using Catalyst
#Summary(pl.UTF-8):	
Name:		perl-CatalystX-ListFramework-Builder
Version:	0.38
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CatalystX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ce4be405703c52dadca7964e8aa380d8
URL:		http://search.cpan.org/dist/CatalystX-ListFramework-Builder/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Catalyst::View::JSON)
BuildRequires:	perl-Catalyst >= 5.70
BuildRequires:	perl-Catalyst-Action-RenderView
BuildRequires:	perl-Catalyst-Model-DBIC-Schema
BuildRequires:	perl-Catalyst-View-TT
BuildRequires:	perl-MRO-Compat
BuildRequires:	perl(Test::WWW::Mechanize) >= 1.16
BuildRequires:	perl(Test::WWW::Mechanize::Catalyst) >= 0.42
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module contains an application which will automatically construct a web
interface for a database on the fly. The web interface supports Create,
Retrieve, Update, Delete and Search operations.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README TODO
%{perl_vendorlib}/CatalystX/ListFramework/*.pm
%{perl_vendorlib}/CatalystX/ListFramework/Builder
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
