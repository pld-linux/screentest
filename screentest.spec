Summary:	The CRT screen quality testing utility
Summary(pl):	Narzędzie do testowania jakości wyświetlacza CRT
Name:		screentest
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.fi.muni.cz/pub/linux/people/jan_kasprzak/screentest/%{name}-%{version}.tar.gz
# Source0-md5:	c44d3f97874f0675b6c31cd1191f9871
URL:		http://www.fi.muni.cz/~kas/screentest/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Screentest is a simple program which displays various patterns
(colors, circles, grids, text) on your screen in order to allow you to
evaluate the quality of your CRT monitor (sharpness, linearity, etc).

%description -l pl
Screentest jest prostym programem wyświetlającym różne wzory (kolory,
okręgi, siatki, tekst) na twoim wyświetlaczu CRT w celu umożliwienia
określenia jego jakości (ostrość, liniowość itp).

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} screentest

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install screentest $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog NEW_TESTS NEWS AUTHORS
%attr(755,root,root) %{_bindir}/*
